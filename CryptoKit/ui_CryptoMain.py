# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CryptoMain.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QWidget)

class Ui_CryptoMain(object):
    def setupUi(self, CryptoMain):
        if not CryptoMain.objectName():
            CryptoMain.setObjectName(u"CryptoMain")
        CryptoMain.resize(813, 569)
        CryptoMain.setStyleSheet(u"background:#222f4d")
        self.label = QLabel(CryptoMain)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 20, 211, 71))
        font = QFont()
        font.setPointSize(37)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:white;")
        self.label_2 = QLabel(CryptoMain)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 200, 221, 51))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:white;")
        self.AESChoice = QRadioButton(CryptoMain)
        self.AESChoice.setObjectName(u"AESChoice")
        self.AESChoice.setGeometry(QRect(90, 260, 301, 31))
        font2 = QFont()
        font2.setPointSize(14)
        self.AESChoice.setFont(font2)
        self.AESChoice.setStyleSheet(u"color:white;\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       #00a1ca;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.AUTHChoice = QRadioButton(CryptoMain)
        self.AUTHChoice.setObjectName(u"AUTHChoice")
        self.AUTHChoice.setGeometry(QRect(90, 310, 301, 31))
        self.AUTHChoice.setFont(font2)
        self.AUTHChoice.setStyleSheet(u"color:white;\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       #00a1ca;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       white;\n"
"    border:                 2px solid white;\n"
"}")
        self.next = QPushButton(CryptoMain)
        self.next.setObjectName(u"next")
        self.next.setGeometry(QRect(710, 530, 90, 30))
        self.next.setStyleSheet(u"background:#00a1ca;\n"
"color: black;\n"
"border-radius: 6px;")

        self.retranslateUi(CryptoMain)

        QMetaObject.connectSlotsByName(CryptoMain)
    # setupUi

    def retranslateUi(self, CryptoMain):
        CryptoMain.setWindowTitle(QCoreApplication.translate("CryptoMain", u"Form", None))
        self.label.setText(QCoreApplication.translate("CryptoMain", u"CryptoKit", None))
        self.label_2.setText(QCoreApplication.translate("CryptoMain", u"Select Operation:", None))
        self.AESChoice.setText(QCoreApplication.translate("CryptoMain", u"AES Encryption and Decryption", None))
        self.AUTHChoice.setText(QCoreApplication.translate("CryptoMain", u"Authentication", None))
        self.next.setText(QCoreApplication.translate("CryptoMain", u"Next", None))
    # retranslateUi

