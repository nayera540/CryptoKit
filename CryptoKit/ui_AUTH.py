# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AUTH.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

class Ui_AUTH(object):
    def setupUi(self, AUTH):
        if not AUTH.objectName():
            AUTH.setObjectName(u"AUTH")
        AUTH.resize(884, 709)
        AUTH.setStyleSheet(u"background:#222f4d")
        self.header = QLabel(AUTH)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(0, 0, 281, 41))
        font = QFont()
        font.setPointSize(19)
        self.header.setFont(font)
        self.header.setStyleSheet(u"color:white;")
        self.label = QLabel(AUTH)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 70, 161, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color:white;")
        self.label_2 = QLabel(AUTH)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 140, 161, 31))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color:white;")
        self.label_3 = QLabel(AUTH)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 210, 161, 31))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color:white;")
        self.sentMessage = QLineEdit(AUTH)
        self.sentMessage.setObjectName(u"sentMessage")
        self.sentMessage.setGeometry(QRect(180, 80, 671, 28))
        self.sentMessage.setStyleSheet(u"background:#f9f8fa;\n"
"color:balck;\n"
"border-radius: 6px;")
        self.receivedMessage = QLineEdit(AUTH)
        self.receivedMessage.setObjectName(u"receivedMessage")
        self.receivedMessage.setGeometry(QRect(180, 140, 671, 28))
        self.receivedMessage.setStyleSheet(u"background:#f9f8fa;\n"
"color:balck;\n"
"border-radius: 6px;")
        self.key = QLineEdit(AUTH)
        self.key.setObjectName(u"key")
        self.key.setGeometry(QRect(180, 210, 671, 28))
        self.key.setStyleSheet(u"background:#f9f8fa;\n"
"color:balck;\n"
"border-radius: 6px;")
        self.label_4 = QLabel(AUTH)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 310, 151, 31))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color:white;")
        self.label_5 = QLabel(AUTH)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 380, 151, 41))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color:white;")
        self.label_6 = QLabel(AUTH)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 470, 151, 31))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color:white;")
        self.confidentialityOutput = QTextBrowser(AUTH)
        self.confidentialityOutput.setObjectName(u"confidentialityOutput")
        self.confidentialityOutput.setGeometry(QRect(180, 390, 256, 28))
        self.confidentialityOutput.setStyleSheet(u"background:#f9f8fa;\n"
"color:balck;\n"
"border-radius: 6px;")
        self.authOutput = QTextBrowser(AUTH)
        self.authOutput.setObjectName(u"authOutput")
        self.authOutput.setGeometry(QRect(180, 470, 256, 28))
        self.authOutput.setStyleSheet(u"background:#f9f8fa;\n"
"color:balck;\n"
"border-radius: 6px;")
        self.run = QPushButton(AUTH)
        self.run.setObjectName(u"run")
        self.run.setGeometry(QRect(180, 260, 90, 30))
        self.run.setStyleSheet(u"background:#00a1ca;\n"
"color: black;\n"
"border-radius: 6px;")
        self.back = QPushButton(AUTH)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(10, 650, 90, 30))
        self.back.setStyleSheet(u"background:#00a1ca;\n"
"color: black;\n"
"border-radius: 6px;")

        self.retranslateUi(AUTH)

        QMetaObject.connectSlotsByName(AUTH)
    # setupUi

    def retranslateUi(self, AUTH):
        AUTH.setWindowTitle(QCoreApplication.translate("AUTH", u"Form", None))
        self.header.setText(QCoreApplication.translate("AUTH", u"Authentication", None))
        self.label.setText(QCoreApplication.translate("AUTH", u"Sent Message", None))
        self.label_2.setText(QCoreApplication.translate("AUTH", u"Received Message", None))
        self.label_3.setText(QCoreApplication.translate("AUTH", u"Key", None))
        self.label_4.setText(QCoreApplication.translate("AUTH", u"Output", None))
        self.label_5.setText(QCoreApplication.translate("AUTH", u"Confidentiality", None))
        self.label_6.setText(QCoreApplication.translate("AUTH", u"Authentication", None))
        self.run.setText(QCoreApplication.translate("AUTH", u"Run", None))
        self.back.setText(QCoreApplication.translate("AUTH", u"Back", None))
    # retranslateUi

