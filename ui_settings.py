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
    QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        if not SettingsWidget.objectName():
            SettingsWidget.setObjectName(u"SettingsWidget")
        SettingsWidget.resize(620, 442)
        font = QFont()
        font.setPointSize(14)
        SettingsWidget.setFont(font)
        icon = QIcon()
        icon.addFile(u":/images/icons8-settings-94.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        SettingsWidget.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(SettingsWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(SettingsWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(27, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.result_folder_line_edit = QLineEdit(SettingsWidget)
        self.result_folder_line_edit.setObjectName(u"result_folder_line_edit")
        self.result_folder_line_edit.setFont(font)

        self.horizontalLayout_4.addWidget(self.result_folder_line_edit)

        self.result_folder_browse_button = QPushButton(SettingsWidget)
        self.result_folder_browse_button.setObjectName(u"result_folder_browse_button")
        self.result_folder_browse_button.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/images/folder-1485.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.result_folder_browse_button.setIcon(icon1)
        self.result_folder_browse_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.result_folder_browse_button)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(SettingsWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.result_file_name_line_edit = QLineEdit(SettingsWidget)
        self.result_file_name_line_edit.setObjectName(u"result_file_name_line_edit")
        self.result_file_name_line_edit.setFont(font)

        self.horizontalLayout.addWidget(self.result_file_name_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(SettingsWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.horizontalSpacer_3 = QSpacerItem(16, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.log_folder_line_edit = QLineEdit(SettingsWidget)
        self.log_folder_line_edit.setObjectName(u"log_folder_line_edit")
        self.log_folder_line_edit.setFont(font)

        self.horizontalLayout_5.addWidget(self.log_folder_line_edit)

        self.log_folder_browse_button = QPushButton(SettingsWidget)
        self.log_folder_browse_button.setObjectName(u"log_folder_browse_button")
        self.log_folder_browse_button.setFont(font)
        self.log_folder_browse_button.setIcon(icon1)
        self.log_folder_browse_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.log_folder_browse_button)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(SettingsWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(19, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.log_file_name_line_edit = QLineEdit(SettingsWidget)
        self.log_file_name_line_edit.setObjectName(u"log_file_name_line_edit")
        self.log_file_name_line_edit.setFont(font)

        self.horizontalLayout_2.addWidget(self.log_file_name_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.keep_settings_checkbox = QCheckBox(SettingsWidget)
        self.keep_settings_checkbox.setObjectName(u"keep_settings_checkbox")
        self.keep_settings_checkbox.setFont(font)
        self.keep_settings_checkbox.setChecked(True)

        self.verticalLayout.addWidget(self.keep_settings_checkbox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(SettingsWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_6 = QSpacerItem(62, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.protocol_combo_box = QComboBox(SettingsWidget)
        self.protocol_combo_box.setObjectName(u"protocol_combo_box")
        self.protocol_combo_box.setFont(font)

        self.horizontalLayout_3.addWidget(self.protocol_combo_box)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_3.setStretch(3, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.settings_ok_button = QPushButton(SettingsWidget)
        self.settings_ok_button.setObjectName(u"settings_ok_button")

        self.horizontalLayout_6.addWidget(self.settings_ok_button)

        self.settings_cancel_button = QPushButton(SettingsWidget)
        self.settings_cancel_button.setObjectName(u"settings_cancel_button")

        self.horizontalLayout_6.addWidget(self.settings_cancel_button)

        self.settings_apply_button = QPushButton(SettingsWidget)
        self.settings_apply_button.setObjectName(u"settings_apply_button")

        self.horizontalLayout_6.addWidget(self.settings_apply_button)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.retranslateUi(SettingsWidget)

        QMetaObject.connectSlotsByName(SettingsWidget)
    # setupUi

    def retranslateUi(self, SettingsWidget):
        SettingsWidget.setWindowTitle(QCoreApplication.translate("SettingsWidget", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("SettingsWidget", u"Result folder:", None))
        self.result_folder_browse_button.setText(QCoreApplication.translate("SettingsWidget", u"Browse", None))
        self.label.setText(QCoreApplication.translate("SettingsWidget", u"Result file name:", None))
        self.label_5.setText(QCoreApplication.translate("SettingsWidget", u"Log file folder:", None))
        self.log_folder_browse_button.setText(QCoreApplication.translate("SettingsWidget", u"Browse", None))
        self.label_2.setText(QCoreApplication.translate("SettingsWidget", u"Log file name:", None))
        self.keep_settings_checkbox.setText(QCoreApplication.translate("SettingsWidget", u"Keep Active Directory configuration on application close", None))
        self.label_3.setText(QCoreApplication.translate("SettingsWidget", u"Protocol:", None))
        self.settings_ok_button.setText(QCoreApplication.translate("SettingsWidget", u"OK", None))
        self.settings_cancel_button.setText(QCoreApplication.translate("SettingsWidget", u"Cancel", None))
        self.settings_apply_button.setText(QCoreApplication.translate("SettingsWidget", u"Apply", None))
    # retranslateUi

