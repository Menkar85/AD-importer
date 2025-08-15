from PySide6.QtWidgets import QApplication
import sys
import logging
import os
import tempfile
import pickle

from mainwindow import MainWindow
from utils.i18n_manager import I18nManager

app = QApplication(sys.argv)
i18n = I18nManager(app)
try:
    with open('data/lang.pkl', 'rb') as fp:
        i18n.load_translations(pickle.load(fp)['lang_code'])
except:
    i18n.load_translations('en')

window = MainWindow(app)
window.show()
temp_dir_path = tempfile.gettempdir()
temp_log_file = os.path.join(temp_dir_path, window.log_file_name)

logging.basicConfig(filename=temp_log_file, filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

app.exec()
