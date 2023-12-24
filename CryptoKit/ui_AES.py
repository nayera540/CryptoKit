# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AES.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

class Ui_AES(object):
    def setupUi(self, AES):
        if not AES.objectName():
            AES.setObjectName(u"AES")
        AES.resize(884, 709)
        AES.setStyleSheet(u"background:#222f4d")
        self.header = QLabel(AES)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(10, 0, 281, 41))
        font = QFont()
        font.setPointSize(19)
        self.header.setFont(font)
        self.header.setStyleSheet(u"color:white;")
        self.mode = QLabel(AES)
        self.mode.setObjectName(u"mode")
        self.mode.setGeometry(QRect(10, 160, 57, 16))
        font1 = QFont()
        font1.setPointSize(14)
        self.mode.setFont(font1)
        self.mode.setStyleSheet(u"color:white;")
        self.modeOptions = QComboBox(AES)
        self.modeOptions.addItem("")
        self.modeOptions.addItem("")
        self.modeOptions.setObjectName(u"modeOptions")
        self.modeOptions.setGeometry(QRect(110, 150, 751, 31))
        self.modeOptions.setStyleSheet(u"QComboBox {\n"
"    background-color: #f9f8fa;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #f9f8fa;\n"
"    color: black;\n"
"    border-radius: 6px;\n"
"    selection-background-color: #aeb0b3; /* Change this color for the selected item in the dropdown list */\n"
"}\n"
"\n"
"")
        self.enc = QPushButton(AES)
        self.enc.setObjectName(u"enc")
        self.enc.setGeometry(QRect(110, 350, 90, 30))
        self.enc.setStyleSheet(u"background:#00a1ca;\n"
"color: black;\n"
"border-radius: 6px;")
        self.dec = QPushButton(AES)
        self.dec.setObjectName(u"dec")
        self.dec.setGeometry(QRect(210, 350, 90, 30))
        self.dec.setStyleSheet(u"background:#00a1ca;\n"
"color: black;\n"
"border-radius: 6px;")
        self.output = QLabel(AES)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(10, 410, 661, 31))
        self.output.setFont(font1)
        self.output.setStyleSheet(u"color:white;")
        self.outputText = QTextBrowser(AES)
        self.outputText.setObjectName(u"outputText")
        self.outputText.setGeometry(QRect(10, 450, 851, 191))
        self.outputText.setStyleSheet(u"background:#f9f8fa;\n"
"color:balck;\n"
"border-radius: 6px;")
        self.save = QPushButton(AES)
        self.save.setObjectName(u"save")
        self.save.setGeometry(QRect(770, 650, 90, 30))
        self.save.setStyleSheet(u"background:#00a1ca;\n"
"color: black;\n"
"border-radius: 6px;")
        self.label_2 = QLabel(AES)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 230, 91, 16))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:white;")
        self.initVector = QLineEdit(AES)
        self.initVector.setObjectName(u"initVector")
        self.initVector.setGeometry(QRect(110, 230, 751, 21))
        self.initVector.setStyleSheet(u"background:#f9f8fa;\n"
"color:balck;\n"
"border-radius: 6px;")
        self.filePath = QLineEdit(AES)
        self.filePath.setObjectName(u"filePath")
        self.filePath.setGeometry(QRect(110, 89, 751, 21))
        self.filePath.setStyleSheet(u"background:#f9f8fa;\n"
"color:balck;\n"
"border-radius: 6px;")
        self.file = QLabel(AES)
        self.file.setObjectName(u"file")
        self.file.setGeometry(QRect(10, 90, 91, 23))
        self.file.setFont(font1)
        self.file.setStyleSheet(u"color:white;")
        self.key = QLineEdit(AES)
        self.key.setObjectName(u"key")
        self.key.setGeometry(QRect(110, 300, 751, 21))
        self.key.setStyleSheet(u"background:#f9f8fa;\n"
"color:balck;\n"
"border-radius: 6px;")
        self.label = QLabel(AES)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 300, 41, 23))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color:white;")
        self.back = QPushButton(AES)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(10, 650, 90, 30))
        self.back.setStyleSheet(u"background:#00a1ca;\n"
"color: black;\n"
"border-radius: 6px;")

        self.retranslateUi(AES)

        QMetaObject.connectSlotsByName(AES)
    # setupUi

    def retranslateUi(self, AES):
        AES.setWindowTitle(QCoreApplication.translate("AES", u"Widget", None))
        self.header.setText(QCoreApplication.translate("AES", u"AES-Symmetric Ciphers", None))
        self.mode.setText(QCoreApplication.translate("AES", u"Mode", None))
        self.modeOptions.setItemText(0, QCoreApplication.translate("AES", u"ECB (electronic code book)", None))
        self.modeOptions.setItemText(1, QCoreApplication.translate("AES", u"CBC (cipher block chaining)", None))

        self.enc.setText(QCoreApplication.translate("AES", u"Encrypt", None))
        self.dec.setText(QCoreApplication.translate("AES", u"Decrypt", None))
        self.output.setText(QCoreApplication.translate("AES", u"Output", None))
        self.save.setText(QCoreApplication.translate("AES", u"Save", None))
        self.label_2.setText(QCoreApplication.translate("AES", u"Init. vector", None))
        self.file.setText(QCoreApplication.translate("AES", u"File", None))
        self.label.setText(QCoreApplication.translate("AES", u"Key", None))
        self.back.setText(QCoreApplication.translate("AES", u"Back", None))
    # retranslateUi

