from PySide6.QtWidgets import QWidget
import pickle
import os
from ui_settings import Ui_SettingsWidget

VERSION = "0.0.1-alpha"
AD_SETTINGS = './data/ad.pkl'
APP_SETTINGS = './data/app.pkl'

if not os.path.exists(os.path.dirname(APP_SETTINGS)):
    os.makedirs(os.path.dirname(APP_SETTINGS))


class SettingsWidget(Ui_SettingsWidget, QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Settings")

        # data init
        self.parent = parent
        self.result_folder = parent.result_folder or ""
        self.result_file_name = parent.result_file_name or "result"
        self.log_folder = parent.log_folder or ""
        self.log_file_name = parent.log_file_name or "log"
        self.keep_settings = parent.keep_settings
        self.protocol = parent.protocol or "LDAP"

        self.result_folder_line_edit.setText(self.result_folder)
        self.result_file_name_line_edit.setText(self.result_file_name)
        self.log_folder_line_edit.setText(self.log_folder)
        self.log_file_name_line_edit.setText(self.log_file_name)

        self.result_folder_browse_button.clicked.connect(self._result_browse_button_clicked)
        self.log_folder_browse_button.clicked.connect(self._log_browse_button_clicked)
        self.settings_ok_button.clicked.connect(self._ok_button_clicked)
        self.settings_apply_button.clicked.connect(self._apply_button_clicked)
        self.settings_cancel_button.clicked.connect(self._cancel_button_clicked)

    # slots
    def _result_browse_button_clicked(self):
        # TODO: browse button for result via get path
        pass

    def _log_browse_button_clicked(self):
        # TODO: browse button for log via get path
        pass

    def _ok_button_clicked(self):
        self._apply_button_clicked()
        self._cancel_button_clicked()

    def _apply_button_clicked(self):
        app_settings = {
            'result_folder': self.result_folder,
            'result_file_name': self.result_file_name,
            'log_folder': self.log_folder,
            'log_file_name': self.log_file_name,
            'keep_settings': self.keep_settings,
            'protocol': self.protocol,
        }
        with open(APP_SETTINGS, 'wb+') as fp:
            pickle.dump(app_settings, fp)

        for attr, value in app_settings.items():
            setattr(self.parent, attr, value)


    def _cancel_button_clicked(self):
        self.destroy()


