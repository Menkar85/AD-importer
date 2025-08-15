from PySide6.QtWidgets import QApplication
import sys
import logging
import os
import tempfile

from mainwindow import MainWindow



app = QApplication(sys.argv)
window = MainWindow(app)
window.show()
temp_dir_path = tempfile.gettempdir()
temp_log_file = os.path.join(temp_dir_path, window.log_file_name)

logging.basicConfig(filename=temp_log_file, filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)


app.exec()
