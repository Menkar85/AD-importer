from PySide6.QtWidgets import QMainWindow, QWidget
from ui_mainwindow import Ui_main_window


class MainWindow(Ui_main_window, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("AD user import tool")