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
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(f"AD user import tool v.{VERSION}")
        self.app = app
        self.settings_window = None

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
        self.username_line_edit.editingFinished.connect(self._username_line_edit_finished)
        self.password_line_edit.editingFinished.connect(self._password_line_edit_finished)
        self.upn_suffix_line_edit.editingFinished.connect(self._upn_suffix_line_edit_finished)
        self.destination_ou_line_edit.editingFinished.connect(self._destination_ou_line_edit_finished)

    # slots
    def settings_open(self):
        self.settings_window = SettingsWidget(self)
        self.settings_window.show()
        logger.info('Settings window opened.')

    def quit(self):
        self.app.quit()

    def switch_english(self):
        # TODO: Realize i18n
        print("english selected")

    def switch_russian(self):
        # TODO: Realize i18n
        print("russian selected")

    def about(self):
        QMessageBox.information(self, "About", "Software for batch import of users into Active Directory.")

    def about_qt(self):
        self.app.aboutQt()

    def _test_button_clicked(self):
        self.ad_server = self.ad_server_line_edit.text()
        try:
            socket.gethostbyname(self.ad_server)
            QMessageBox.information(self, "Success", 'Server name successfully validated.')
            logger.debug(f"{self.ad_server} name dns was detected.")
        except socket.gaierror:
            QMessageBox.critical(self, "Error", "Server not found! Please check server name or that PC is in domain.")

    def _browse_button_clicked(self):
        file, used_filter = QFileDialog.getOpenFileName(filter='Excel files (*.xlsx *.xls)')
        self.source_file = file
        logger.debug(f"Get source data from {file}")
        self.source_file_line_edit.setText(file)

    def _result_save_as_button_clicked(self):
        self.result_file_name, used_filter = QFileDialog.getSaveFileName(self, filter="Excel files (*.xlsx)")
        logger.debug(f"File name for saving results is {self.result_file_name}")
        self._result_file_path_updated(self.result_file_name)

    def _preview_button_clicked(self):
        self._display_table_data(self.source_file)

    def _start_import_button_clicked(self):
        ret = QMessageBox.warning(self, "Warning",
                                  "Next step will apply changes to AD.\nPlease verify correct destination OU and confirm user import.",
                                  buttons=QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        if ret == QMessageBox.StandardButton.Ok:
            logger.info("Starting users import...")
            if self.keep_settings:
                self._save_ad_settings()
            import_data = get_excel_data(self.source_file, has_headers=True)
            logger.info(f"Got data from {self.source_file}")
            import_data = build_import_data(import_data, self.upn_suffix)
            logger.debug(f"Built import data from {self.source_file}")
            try:
                res = import_ad_users(self.ad_server, self.destination_ou, self.ad_user, self.ad_password,
                                      self.protocol, import_data, self.result_file_name)
            except Exception as e:
                logger.critical(f"Critical error occurred during import {e}")
                QMessageBox.critical(self, 'Errors during import',
                                     f'During import following error occurred: {e}. \nPlease check log file {self.log_file_name} for details.',
                                     buttons=QMessageBox.StandardButton.Ok)
            else:
                if res == 0:
                    logger.info("Import completed successfully.")
                    QMessageBox.information(self, 'Success', 'Import completed.', buttons=QMessageBox.StandardButton.Ok)
                else:
                    logger.warning(f"Totally {res} problem(s) occurred during import")
                    QMessageBox.warning(self, 'Warning',
                                        f'{res} problem(s) occurred during import. \nPlease check results file and logs for details.',
                                        buttons=QMessageBox.StandardButton.Ok)
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
        ret = QMessageBox.question(self, "Confirmation", "Do you really want to quit?",
                                   buttons=QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        if ret == QMessageBox.StandardButton.Ok:
            self.app.quit()
        else:
            pass

    def _username_line_edit_finished(self):
        self.ad_user = self.username_line_edit.text()

    def _password_line_edit_finished(self):
        self.ad_password = self.password_line_edit.text()

    def _upn_suffix_line_edit_finished(self):
        self.upn_suffix = self.upn_suffix_line_edit.text()

    def _destination_ou_line_edit_finished(self):
        self.destination_ou = self.destination_ou_line_edit.text()

    # methods
    def _save_ad_settings(self):
        ad_settings = {
            'ad_server': self.ad_server,
            'ad_user': self.ad_user,
            'upn_suffix': self.upn_suffix,
            'destination_ou': self.destination_ou,
            'source_file': self.source_file,
        }
        with open(AD_SETTINGS, 'wb') as fp:
            pickle.dump(ad_settings, fp)
        logging.debug('AD settings saved successfully')

    def _retrieve_ad_settings(self):
        try:
            with open(AD_SETTINGS, 'rb') as fp:
                app_settings = pickle.load(fp)
                self.ad_server = app_settings['ad_server']
                self.ad_user = app_settings['ad_user']
                self.upn_suffix = app_settings['upn_suffix']
                self.destination_ou = app_settings['destination_ou']
                self.source_file = app_settings['source_file']
        except:
            pass

    def _retrieve_app_settings(self):
        try:
            with open(APP_SETTINGS, 'rb') as fp:
                app_settings = pickle.load(fp)
                self.log_folder = app_settings['log_folder']
                self.keep_settings = app_settings['keep_settings']
                self.protocol = app_settings['protocol']
                logger.debug("App settings retrieved successfully")
        except Exception as e:
            logger.warning(f"App settings were not retrieved due to {e}")
            pass

    def _result_file_path_updated(self, text):
        self.result_file_line_edit.setText(text)

    def _display_table_data(self, result_path):
        preview_model = QStandardItemModel()
        source = get_excel_data(result_path, has_headers=True)
        preview_model.setHorizontalHeaderLabels([str(header) for header in source['headers']])
        for row_data in source['data']:
            items = [QStandardItem(str(cell) if cell is not None else "") for cell in row_data]
            preview_model.appendRow(items)
        self.preview_table_view.setModel(preview_model)
        self.preview_table_view.resizeColumnsToContents()
