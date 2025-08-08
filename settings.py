from PySide6.QtWidgets import QWidget

from ui_settings import Ui_SettingsWidget


class SettingsWidget(Ui_SettingsWidget, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Settings")