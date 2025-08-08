# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableView, QVBoxLayout, QWidget)
import resource_rc

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(1109, 863)
        self.actionEnglish = QAction(main_window)
        self.actionEnglish.setObjectName(u"actionEnglish")
        icon = QIcon()
        icon.addFile(u":/images/icons8-united-kingdom-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionEnglish.setIcon(icon)
        self.actionRussian = QAction(main_window)
        self.actionRussian.setObjectName(u"actionRussian")
        icon1 = QIcon()
        icon1.addFile(u":/images/icons8-russia-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionRussian.setIcon(icon1)
        self.actionAbout = QAction(main_window)
        self.actionAbout.setObjectName(u"actionAbout")
        icon2 = QIcon()
        icon2.addFile(u":/images/aboutQtIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAbout.setIcon(icon2)
        self.actionAbout_Qt = QAction(main_window)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        icon3 = QIcon()
        icon3.addFile(u":/images/icons8-about-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAbout_Qt.setIcon(icon3)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.settings_group_box = QGroupBox(self.centralwidget)
        self.settings_group_box.setObjectName(u"settings_group_box")
        font = QFont()
        font.setPointSize(14)
        self.settings_group_box.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.settings_group_box)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.settings_group_box)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.settings_group_box)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.button_test = QPushButton(self.settings_group_box)
        self.button_test.setObjectName(u"button_test")
        self.button_test.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.button_test)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.settings_group_box)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.settings_group_box)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.settings_group_box)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.settings_group_box)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.settings_group_box)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.settings_group_box)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_4.addWidget(self.lineEdit_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addWidget(self.settings_group_box)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_5.addWidget(self.lineEdit_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineEdit_6 = QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_6.addWidget(self.lineEdit_6)

        self.button_browse = QPushButton(self.groupBox)
        self.button_browse.setObjectName(u"button_browse")
        icon4 = QIcon()
        icon4.addFile(u":/images/folder-1485.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_browse.setIcon(icon4)

        self.horizontalLayout_6.addWidget(self.button_browse)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.tableView = QTableView(self.groupBox)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableView.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.tableView.setWordWrap(False)

        self.verticalLayout_3.addWidget(self.tableView)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/images/icons8-view-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/images/icons8-export-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon6)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u":/images/icons8-cancel-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon7)
        self.pushButton_3.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.pushButton_3)

        self.horizontalLayout_7.setStretch(0, 5)
        self.horizontalLayout_7.setStretch(1, 5)
        self.horizontalLayout_7.setStretch(2, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1109, 33))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuLanguage = QMenu(self.menubar)
        self.menuLanguage.setObjectName(u"menuLanguage")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuQuit = QMenu(self.menubar)
        self.menuQuit.setObjectName(u"menuQuit")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuLanguage.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuQuit.menuAction())
        self.menuLanguage.addAction(self.actionEnglish)
        self.menuLanguage.addAction(self.actionRussian)
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addAction(self.actionAbout_Qt)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"MainWindow", None))
        self.actionEnglish.setText(QCoreApplication.translate("main_window", u"English", None))
        self.actionRussian.setText(QCoreApplication.translate("main_window", u"Russian", None))
        self.actionAbout.setText(QCoreApplication.translate("main_window", u"About", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("main_window", u"About Qt", None))
        self.settings_group_box.setTitle(QCoreApplication.translate("main_window", u"Active Directory Configuration", None))
        self.label.setText(QCoreApplication.translate("main_window", u"AD Server name:", None))
        self.button_test.setText(QCoreApplication.translate("main_window", u"Test", None))
        self.label_2.setText(QCoreApplication.translate("main_window", u"User name:", None))
        self.label_3.setText(QCoreApplication.translate("main_window", u"Password:", None))
        self.label_4.setText(QCoreApplication.translate("main_window", u"UPN-suffix:", None))
        self.groupBox.setTitle(QCoreApplication.translate("main_window", u"Import configuration", None))
        self.label_5.setText(QCoreApplication.translate("main_window", u"Destination OU:", None))
        self.label_6.setText(QCoreApplication.translate("main_window", u"Source file:", None))
        self.button_browse.setText(QCoreApplication.translate("main_window", u"Browse", None))
        self.pushButton.setText(QCoreApplication.translate("main_window", u"Preview file", None))
        self.pushButton_2.setText(QCoreApplication.translate("main_window", u"Start importing", None))
        self.pushButton_3.setText(QCoreApplication.translate("main_window", u"Cancel", None))
        self.menuSettings.setTitle(QCoreApplication.translate("main_window", u"Settings", None))
        self.menuLanguage.setTitle(QCoreApplication.translate("main_window", u"Language", None))
        self.menuAbout.setTitle(QCoreApplication.translate("main_window", u"About", None))
        self.menuQuit.setTitle(QCoreApplication.translate("main_window", u"Quit", None))
    # retranslateUi

