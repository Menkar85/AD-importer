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
        main_window.resize(1109, 944)
        font = QFont()
        font.setPointSize(9)
        main_window.setFont(font)
        icon = QIcon()
        icon.addFile(u":/images/referal_17752807.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        main_window.setWindowIcon(icon)
        self.actionEnglish = QAction(main_window)
        self.actionEnglish.setObjectName(u"actionEnglish")
        self.actionEnglish.setEnabled(True)
        icon1 = QIcon()
        icon1.addFile(u":/images/icons8-united-kingdom-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionEnglish.setIcon(icon1)
        self.actionRussian = QAction(main_window)
        self.actionRussian.setObjectName(u"actionRussian")
        icon2 = QIcon()
        icon2.addFile(u":/images/icons8-russia-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionRussian.setIcon(icon2)
        self.actionAbout = QAction(main_window)
        self.actionAbout.setObjectName(u"actionAbout")
        icon3 = QIcon()
        icon3.addFile(u":/images/aboutQtIcon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAbout.setIcon(icon3)
        self.actionAbout_Qt = QAction(main_window)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        icon4 = QIcon()
        icon4.addFile(u":/images/icons8-about-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAbout_Qt.setIcon(icon4)
        self.actionSettings = QAction(main_window)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionQuit = QAction(main_window)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.settings_group_box = QGroupBox(self.centralwidget)
        self.settings_group_box.setObjectName(u"settings_group_box")
        font1 = QFont()
        font1.setPointSize(14)
        self.settings_group_box.setFont(font1)
        self.horizontalLayout_2 = QHBoxLayout(self.settings_group_box)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.settings_group_box)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.settings_group_box)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.settings_group_box)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.settings_group_box)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_8 = QLabel(self.settings_group_box)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_8)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ad_server_line_edit = QLineEdit(self.settings_group_box)
        self.ad_server_line_edit.setObjectName(u"ad_server_line_edit")

        self.horizontalLayout.addWidget(self.ad_server_line_edit)

        self.test_button = QPushButton(self.settings_group_box)
        self.test_button.setObjectName(u"test_button")
        self.test_button.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.test_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.username_line_edit = QLineEdit(self.settings_group_box)
        self.username_line_edit.setObjectName(u"username_line_edit")

        self.verticalLayout.addWidget(self.username_line_edit)

        self.password_line_edit = QLineEdit(self.settings_group_box)
        self.password_line_edit.setObjectName(u"password_line_edit")
        self.password_line_edit.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.password_line_edit)

        self.upn_suffix_line_edit = QLineEdit(self.settings_group_box)
        self.upn_suffix_line_edit.setObjectName(u"upn_suffix_line_edit")

        self.verticalLayout.addWidget(self.upn_suffix_line_edit)

        self.email_domain_line_edit = QLineEdit(self.settings_group_box)
        self.email_domain_line_edit.setObjectName(u"email_domain_line_edit")

        self.verticalLayout.addWidget(self.email_domain_line_edit)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addWidget(self.settings_group_box)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font1)
        self.verticalLayout_8 = QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_6)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_7)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.source_file_line_edit = QLineEdit(self.groupBox)
        self.source_file_line_edit.setObjectName(u"source_file_line_edit")
        self.source_file_line_edit.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.source_file_line_edit)

        self.browse_button = QPushButton(self.groupBox)
        self.browse_button.setObjectName(u"browse_button")
        icon5 = QIcon()
        icon5.addFile(u":/images/folder-1485.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.browse_button.setIcon(icon5)

        self.horizontalLayout_4.addWidget(self.browse_button)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.destination_ou_line_edit = QLineEdit(self.groupBox)
        self.destination_ou_line_edit.setObjectName(u"destination_ou_line_edit")

        self.verticalLayout_7.addWidget(self.destination_ou_line_edit)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.result_file_line_edit = QLineEdit(self.groupBox)
        self.result_file_line_edit.setObjectName(u"result_file_line_edit")

        self.horizontalLayout_3.addWidget(self.result_file_line_edit)

        self.result_save_as_button = QPushButton(self.groupBox)
        self.result_save_as_button.setObjectName(u"result_save_as_button")
        self.result_save_as_button.setIcon(icon5)

        self.horizontalLayout_3.addWidget(self.result_save_as_button)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.preview_table_view = QTableView(self.groupBox)
        self.preview_table_view.setObjectName(u"preview_table_view")
        self.preview_table_view.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.preview_table_view.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.preview_table_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.preview_table_view.setWordWrap(False)

        self.verticalLayout_8.addWidget(self.preview_table_view)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.preview_button = QPushButton(self.centralwidget)
        self.preview_button.setObjectName(u"preview_button")
        self.preview_button.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/images/icons8-view-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.preview_button.setIcon(icon6)
        self.preview_button.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.preview_button)

        self.start_import_button = QPushButton(self.centralwidget)
        self.start_import_button.setObjectName(u"start_import_button")
        self.start_import_button.setFont(font1)
        icon7 = QIcon()
        icon7.addFile(u":/images/icons8-export-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.start_import_button.setIcon(icon7)
        self.start_import_button.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.start_import_button)

        self.cancel_button = QPushButton(self.centralwidget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setFont(font1)
        icon8 = QIcon()
        icon8.addFile(u":/images/icons8-cancel-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cancel_button.setIcon(icon8)
        self.cancel_button.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.cancel_button)

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
        self.menuLanguage.setEnabled(True)
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuLanguage.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuSettings.addAction(self.actionSettings)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionQuit)
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
        self.actionSettings.setText(QCoreApplication.translate("main_window", u"Settings", None))
        self.actionQuit.setText(QCoreApplication.translate("main_window", u"Quit", None))
        self.settings_group_box.setTitle(QCoreApplication.translate("main_window", u"Active Directory Configuration", None))
        self.label.setText(QCoreApplication.translate("main_window", u"AD Server name:", None))
        self.label_2.setText(QCoreApplication.translate("main_window", u"User name:", None))
        self.label_3.setText(QCoreApplication.translate("main_window", u"Password:", None))
        self.label_4.setText(QCoreApplication.translate("main_window", u"UPN-suffix:", None))
        self.label_8.setText(QCoreApplication.translate("main_window", u"E-mail domain:", None))
        self.test_button.setText(QCoreApplication.translate("main_window", u"Test", None))
        self.groupBox.setTitle(QCoreApplication.translate("main_window", u"Import configuration", None))
        self.label_6.setText(QCoreApplication.translate("main_window", u"Source file:", None))
        self.label_5.setText(QCoreApplication.translate("main_window", u"Destination OU:", None))
        self.label_7.setText(QCoreApplication.translate("main_window", u"Save result to:", None))
        self.browse_button.setText(QCoreApplication.translate("main_window", u"Browse", None))
        self.result_save_as_button.setText(QCoreApplication.translate("main_window", u"Save as", None))
        self.preview_button.setText(QCoreApplication.translate("main_window", u"Preview file", None))
        self.start_import_button.setText(QCoreApplication.translate("main_window", u"Start importing", None))
        self.cancel_button.setText(QCoreApplication.translate("main_window", u"Cancel", None))
        self.menuSettings.setTitle(QCoreApplication.translate("main_window", u"Settings", None))
        self.menuLanguage.setTitle(QCoreApplication.translate("main_window", u"Language", None))
        self.menuAbout.setTitle(QCoreApplication.translate("main_window", u"About", None))
    # retranslateUi

