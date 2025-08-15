from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PySide6.QtGui import QStandardItem, QStandardItemModel
import pickle
import socket
import logging
import shutil
import tempfile
import os
from datetime import datetime
from ui_mainwindow import Ui_main_window
from settings import SettingsWidget
from settings import APP_SETTINGS, AD_SETTINGS, VERSION
from utils.xlsxutils import get_excel_data, build_import_data
from utils.ad_utils import import_ad_users

logger = logging.getLogger(__name__)


class MainWindow(Ui_main_window, QMainWindow):
    """Main window class for the AD user import tool.

    This class handles the main user interface and coordinates all operations
    including AD connection testing, file browsing, user import, and settings management.
    """

    def __init__(self, app):
        """Initialize the main window.

        Args:
            app: The QApplication instance.
        """
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"AD user import tool v.{VERSION}")
        self.app = app
        self.settings_window = None
        self.lang_code = None

        # data init
        self.ad_server = None
        self.ad_user = None
        self.ad_password = None
        self.upn_suffix = None
        self.destination_ou = None
        self.source_file = None

        # settings init
        self.result_file_name = None
        self.log_folder = None
        self.log_file_name = f"log_{datetime.now().strftime('%Y_%m_%d_%H_%M')}.txt"
        self.keep_settings = True
        self.protocol = "LDAP"

        self._retrieve_app_settings()
        if self.keep_settings:
            self._retrieve_ad_settings()
            # fill data into linedits
            self.ad_server_line_edit.setText(self.ad_server)
            self.username_line_edit.setText(self.ad_user)
            self.upn_suffix_line_edit.setText(self.upn_suffix)
            self.destination_ou_line_edit.setText(self.destination_ou)

        # menubar
        self.actionSettings.triggered.connect(self.settings_open)
        self.actionQuit.triggered.connect(self.quit)
        self.actionEnglish.triggered.connect(self.switch_english)
        self.actionRussian.triggered.connect(self.switch_russian)
        self.actionAbout.triggered.connect(self.about)
        self.actionAbout_Qt.triggered.connect(self.about_qt)

        # buttons
        self.test_button.clicked.connect(self._test_button_clicked)
        self.browse_button.clicked.connect(self._browse_button_clicked)
        self.result_save_as_button.clicked.connect(self._result_save_as_button_clicked)
        self.preview_button.clicked.connect(self._preview_button_clicked)
        self.start_import_button.clicked.connect(self._start_import_button_clicked)
        self.cancel_button.clicked.connect(self._cancel_button_clicked)

        # Line edits
        self.username_line_edit.editingFinished.connect(
            self._username_line_edit_finished
        )
        self.password_line_edit.editingFinished.connect(
            self._password_line_edit_finished
        )
        self.upn_suffix_line_edit.editingFinished.connect(
            self._upn_suffix_line_edit_finished
        )
        self.destination_ou_line_edit.editingFinished.connect(
            self._destination_ou_line_edit_finished
        )

    # slots
    def settings_open(self):
        """Open the settings window.

        Creates and displays a new SettingsWidget instance.
        """
        self.settings_window = SettingsWidget(self)
        self.settings_window.show()
        logger.info("Settings window opened.")

    def quit(self):
        """Quit the application.

        Terminates the QApplication instance.
        """
        self.app.quit()

    def switch_english(self):
        """Switch application language to English.
        """
        self.lang_code = 'en'
        with open('data/lang.pkl', 'wb') as fp:
            pickle.dump({'lang_code': 'en'}, fp)
        QMessageBox.information(self, "Information", "Please restart app for language change.")

    def switch_russian(self):
        """Switch application language to Russian.
        """
        self.lang_code = 'ru'
        with open('data/lang.pkl', 'wb') as fp:
            pickle.dump({'lang_code': 'ru'}, fp)
        QMessageBox.information(self, "Информация", "Перезагрузите приложение для того, чтобы сменить язык.")

    def about(self):
        """Display about dialog.

        Shows an information dialog with software description.
        """
        QMessageBox.information(
            self, self.tr("About"), self.tr("Software for batch import of users into Active Directory.")
        )

    def about_qt(self):
        """Display Qt about dialog.

        Shows the standard Qt about dialog with version information.
        """
        self.app.aboutQt()

    def _test_button_clicked(self):
        """Handle test button click event.

        Validates the AD server name by performing DNS lookup.
        Shows success or error message based on validation result.
        """
        self.ad_server = self.ad_server_line_edit.text()
        try:
            socket.gethostbyname(self.ad_server)
            QMessageBox.information(
                self, self.tr("Success"), self.tr("Server name successfully validated.")
            )
            logger.debug(f"{self.ad_server} name dns was detected.")
        except socket.gaierror:
            QMessageBox.critical(
                self,
                self.tr("Error"),
                self.tr("Server not found! Please check server name or that PC is in domain."),
            )

    def _browse_button_clicked(self):
        """Handle browse button click event.

        Opens a file dialog to select Excel source file for user import.
        Updates the source file path in the UI.
        """
        file, used_filter = QFileDialog.getOpenFileName(
            filter=self.tr("Excel files (*.xlsx *.xls)")
        )
        self.source_file = file
        logger.debug(f"Get source data from {file}")
        self.source_file_line_edit.setText(file)

    def _result_save_as_button_clicked(self):
        """Handle result save as button click event.

        Opens a file dialog to select where to save the import results.
        Updates the result file path in the UI.
        """
        self.result_file_name, used_filter = QFileDialog.getSaveFileName(
            self, filter=self.tr("Excel files (*.xlsx)")
        )
        logger.debug(f"File name for saving results is {self.result_file_name}")
        self._result_file_path_updated(self.result_file_name)

    def _preview_button_clicked(self):
        """Handle preview button click event.

        Displays the source file data in the preview table.
        """
        self._display_table_data(self.source_file)

    def _start_import_button_clicked(self):
        """Handle start import button click event.

        Initiates the AD user import process. Shows confirmation dialog,
        processes Excel data, imports users to AD, and displays results.
        """
        ret = QMessageBox.warning(
            self,
            self.tr("Warning"),
            self.tr(
                "Next step will apply changes to AD.\nPlease verify correct destination OU and confirm user import."),
            buttons=QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
        )
        if ret == QMessageBox.StandardButton.Ok:
            logger.info("Starting users import...")
            if self.keep_settings:
                self._save_ad_settings()
            import_data = get_excel_data(self.source_file, has_headers=True)
            logger.info(f"Got data from {self.source_file}")
            import_data = build_import_data(import_data, self.upn_suffix)
            logger.debug(f"Built import data from {self.source_file}")
            try:
                res = import_ad_users(
                    self.ad_server,
                    self.destination_ou,
                    self.ad_user,
                    self.ad_password,
                    self.protocol,
                    import_data,
                    self.result_file_name,
                )
            except Exception as e:
                logger.critical(f"Critical error occurred during import {e}")
                QMessageBox.critical(
                    self,
                    "Errors during import",
                    f"{self.tr('During import following error occurred:')} {e}. \n{self.tr('Please check log file')} {self.log_file_name} {self.tr('for details.')}",
                    buttons=QMessageBox.StandardButton.Ok,
                )
            else:
                if res == 0:
                    logger.info("Import completed successfully.")
                    QMessageBox.information(
                        self,
                        self.tr("Success"),
                        self.tr("Import completed."),
                        buttons=QMessageBox.StandardButton.Ok,
                    )
                else:
                    logger.warning(f"Totally {res} problem(s) occurred during import")
                    QMessageBox.warning(
                        self,
                        self.tr("Warning"),
                        f"{res} {self.tr('problem(s) occurred during import. \nPlease check results file and logs for details.')}",
                        buttons=QMessageBox.StandardButton.Ok,
                    )
                self._display_table_data(self.result_file_name)
            finally:
                source_file = os.path.join(tempfile.gettempdir(), self.log_file_name)
                try:
                    logging.shutdown()
                    shutil.move(source_file, self.log_folder)
                except:
                    pass
        else:
            pass

    def _cancel_button_clicked(self):
        """Handle cancel button click event.

        Shows confirmation dialog and quits the application if confirmed.
        """
        ret = QMessageBox.question(
            self,
            self.tr("Confirmation"),
            self.tr("Do you really want to quit?"),
            buttons=QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
        )
        if ret == QMessageBox.StandardButton.Ok:
            self.app.quit()
        else:
            pass

    def _username_line_edit_finished(self):
        """Handle username line edit finished event.

        Updates the ad_user attribute when editing is finished.
        """
        self.ad_user = self.username_line_edit.text()

    def _password_line_edit_finished(self):
        """Handle password line edit finished event.

        Updates the ad_password attribute when editing is finished.
        """
        self.ad_password = self.password_line_edit.text()

    def _upn_suffix_line_edit_finished(self):
        """Handle UPN suffix line edit finished event.

        Updates the upn_suffix attribute when editing is finished.
        """
        self.upn_suffix = self.upn_suffix_line_edit.text()

    def _destination_ou_line_edit_finished(self):
        """Handle destination OU line edit finished event.

        Updates the destination_ou attribute when editing is finished.
        """
        self.destination_ou = self.destination_ou_line_edit.text()

    # methods
    def _save_ad_settings(self):
        """Save AD settings to file.

        Serializes and saves AD configuration settings to a pickle file.
        """
        ad_settings = {
            "ad_server": self.ad_server,
            "ad_user": self.ad_user,
            "upn_suffix": self.upn_suffix,
            "destination_ou": self.destination_ou,
            "source_file": self.source_file,
        }
        with open(AD_SETTINGS, "wb") as fp:
            pickle.dump(ad_settings, fp)
        logging.debug("AD settings saved successfully")

    def _retrieve_ad_settings(self):
        """Retrieve AD settings from file.

        Loads and deserializes AD configuration settings from a pickle file.
        Updates instance attributes with loaded settings.
        """
        try:
            with open(AD_SETTINGS, "rb") as fp:
                app_settings = pickle.load(fp)
                self.ad_server = app_settings["ad_server"]
                self.ad_user = app_settings["ad_user"]
                self.upn_suffix = app_settings["upn_suffix"]
                self.destination_ou = app_settings["destination_ou"]
                self.source_file = app_settings["source_file"]
        except:
            pass

    def _retrieve_app_settings(self):
        """Retrieve application settings from file.

        Loads and deserializes application configuration settings from a pickle file.
        Updates instance attributes with loaded settings.
        """
        try:
            with open(APP_SETTINGS, "rb") as fp:
                app_settings = pickle.load(fp)
                self.log_folder = app_settings["log_folder"]
                self.keep_settings = app_settings["keep_settings"]
                self.protocol = app_settings["protocol"]
                logger.debug("App settings retrieved successfully")
        except Exception as e:
            logger.warning(f"App settings were not retrieved due to {e}")
            pass

    def _result_file_path_updated(self, text):
        """Update result file path in UI.

        Args:
            text (str): The new result file path to display.
        """
        self.result_file_line_edit.setText(text)

    def _display_table_data(self, result_path):
        """Display data in the preview table.

        Loads Excel data from the specified path and displays it in the
        preview table view with proper formatting.

        Args:
            result_path (str): Path to the Excel file to display.
        """
        preview_model = QStandardItemModel()
        source = get_excel_data(result_path, has_headers=True)
        preview_model.setHorizontalHeaderLabels(
            [str(header) for header in source["headers"]]
        )
        for row_data in source["data"]:
            items = [
                QStandardItem(str(cell) if cell is not None else "")
                for cell in row_data
            ]
            preview_model.appendRow(items)
        self.preview_table_view.setModel(preview_model)
        self.preview_table_view.resizeColumnsToContents()
