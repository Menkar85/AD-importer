# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        if not SettingsWidget.objectName():
            SettingsWidget.setObjectName(u"SettingsWidget")
        SettingsWidget.resize(647, 421)
        font = QFont()
        font.setPointSize(14)
        SettingsWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(SettingsWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(SettingsWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(SettingsWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font)

        self.horizontalLayout_4.addWidget(self.lineEdit_3)

        self.pushButton = QPushButton(SettingsWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/images/folder-1485.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(SettingsWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(SettingsWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(SettingsWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(SettingsWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font)

        self.horizontalLayout_5.addWidget(self.lineEdit_4)

        self.pushButton_2 = QPushButton(SettingsWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(SettingsWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(SettingsWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.checkBox = QCheckBox(SettingsWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font)
        self.checkBox.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(SettingsWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.comboBox = QComboBox(SettingsWidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)

        self.horizontalLayout_3.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(SettingsWidget)

        QMetaObject.connectSlotsByName(SettingsWidget)
    # setupUi

    def retranslateUi(self, SettingsWidget):
        SettingsWidget.setWindowTitle(QCoreApplication.translate("SettingsWidget", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("SettingsWidget", u"Result folder:", None))
        self.pushButton.setText(QCoreApplication.translate("SettingsWidget", u"Browse", None))
        self.label.setText(QCoreApplication.translate("SettingsWidget", u"Result file name:", None))
        self.label_5.setText(QCoreApplication.translate("SettingsWidget", u"Log file folder:", None))
        self.pushButton_2.setText(QCoreApplication.translate("SettingsWidget", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("SettingsWidget", u"Log file name", None))
        self.checkBox.setText(QCoreApplication.translate("SettingsWidget", u"Keep Active Directory configuration on application close", None))
        self.label_3.setText(QCoreApplication.translate("SettingsWidget", u"Protocol", None))
    # retranslateUi

