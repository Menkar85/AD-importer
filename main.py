from PySide6.QtWidgets import QApplication
import sys

from mainwindow import MainWindow
from settings import SettingsWidget

app = QApplication(sys.argv)
window = MainWindow()
window.show()

settings = SettingsWidget()
settings.show()



app.exec()