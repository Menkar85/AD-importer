from PySide6.QtWidgets import QMainWindow, QWidget, QMessageBox
import pickle
from ui_mainwindow import Ui_main_window
from settings import SettingsWidget
from settings import APP_SETTINGS, AD_SETTINGS, VERSION



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
        self._retrieve_ad_settings()

        # settings init
        self.result_folder = None
        self.result_file_name = None
        self.log_folder = None
        self.log_file_name = None
        self.keep_settings = True
        self.protocol = "LDAP"

        self._retrieve_app_settings()

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
        self.preview_button.clicked.connect(self._preview_button_clicked)
        self.start_import_button.clicked.connect(self._start_import_button_clicked)
        self.cancel_button.clicked.connect(self._cancel_button_clicked)

    # slots
    def settings_open(self):
        print("settings triggered")
        self.settings_window = SettingsWidget(self)
        self.settings_window.show()

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
        # TODO: Resolve dns name of server. If ok - success window, else - failure window
        pass

    def _browse_button_clicked(self):
        # TODO: Browse window functionality
        pass

    def _preview_button_clicked(self):
        # TODO: loading of excel file into preview window
        pass
    def _start_import_button_clicked(self):
        # TODO: start importing with confirmation window ok - proceed, cancel - back
        pass
    def _cancel_button_clicked(self) :
        # TODO: cancel button - quit with confirmation window
        pass


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
                self.result_folder = app_settings['result_folder']
                self.result_file_name = app_settings['result_file_name']
                self.log_folder = app_settings['log_folder']
                self.log_file_name = app_settings['log_file_name']
                self.keep_settings = app_settings['keep_settings']
                self.protocol = app_settings['protocol']
        except:
            pass
