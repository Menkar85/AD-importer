from PySide6.QtWidgets import QWidget, QFileDialog
import pickle
import os
from ui_settings import Ui_SettingsWidget

VERSION = "0.1.1"
AD_SETTINGS = './data/ad.pkl'
APP_SETTINGS = './data/app.pkl'

if not os.path.exists(os.path.dirname(APP_SETTINGS)):
    os.makedirs(os.path.dirname(APP_SETTINGS))


class SettingsWidget(Ui_SettingsWidget, QWidget):
    """Settings widget for configuring application preferences.
    
    This widget allows users to configure logging settings, protocol preferences,
    and whether to persist settings between sessions.
    """

    def __init__(self, parent):
        """Initialize the settings widget.
        
        Args:
            parent: The parent widget that owns this settings widget.
        """
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(self.tr("Settings"))

        # data init
        self.parent = parent
        self.log_folder = parent.log_folder or ""
        self.keep_settings = parent.keep_settings
        self.protocol = parent.protocol or "LDAP"

        # fields
        self.log_folder_line_edit.setText(self.log_folder)
        self.keep_settings_checkbox.setChecked(self.keep_settings)
        self.log_folder_line_edit.setReadOnly(True)
        self.protocol_combo_box.addItems(['LDAP', 'LDAPS'])
        self.protocol_combo_box.setCurrentText(self.protocol)
        self.protocol_combo_box.currentTextChanged.connect(self._protocol_changed)

        self.log_folder_browse_button.clicked.connect(self._log_browse_button_clicked)
        self.settings_ok_button.clicked.connect(self._ok_button_clicked)
        self.settings_apply_button.clicked.connect(self._apply_button_clicked)
        self.settings_cancel_button.clicked.connect(self._cancel_button_clicked)
        self.keep_settings_checkbox.checkStateChanged.connect(self._keep_settings_checked)

    # slots
    def _log_browse_button_clicked(self):
        """Handle log folder browse button click event.
        
        Opens a directory dialog to select the log folder location.
        Updates the log folder path in the UI and instance attribute.
        """
        directory = QFileDialog.getExistingDirectory()
        self.log_folder = directory
        self.log_folder_line_edit.setText(directory)

    def _ok_button_clicked(self):
        """Handle OK button click event.
        
        Applies the current settings and closes the settings window.
        """
        self._apply_button_clicked()
        self._cancel_button_clicked()

    def _apply_button_clicked(self):
        """Handle apply button click event.
        
        Saves the current settings to file and updates the parent widget
        with the new configuration values.
        """
        app_settings = {
            'log_folder': self.log_folder,
            'keep_settings': self.keep_settings,
            'protocol': self.protocol,
        }
        with open(APP_SETTINGS, 'wb+') as fp:
            pickle.dump(app_settings, fp)

        for attr, value in app_settings.items():
            setattr(self.parent, attr, value)

    def _cancel_button_clicked(self):
        """Handle cancel button click event.
        
        Destroys the settings window without saving changes.
        """
        self.destroy()

    def _protocol_changed(self):
        """Handle protocol combo box change event.
        
        Updates the protocol attribute when a new protocol is selected.
        """
        self.protocol = self.protocol_combo_box.currentText()

    def _keep_settings_checked(self):
        """Handle keep settings checkbox change event.
        
        Updates the keep_settings attribute when the checkbox state changes.
        """
        self.keep_settings = self.keep_settings_checkbox.isChecked()
