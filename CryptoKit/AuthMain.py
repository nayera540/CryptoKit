import os, sys

from PySide6 import QtGui
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QWidget
from ui_AUTH import Ui_AUTH
from AUTH import perform_authentication, confidentiality_authentication
basedir = os.path.dirname(__file__)
class AUTH_Widget(QWidget):
    backClicked = Signal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_AUTH()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'icon.ico')))
        self.setWindowTitle("CryptoKit-AUTH")
        self.setFixedSize(self.size())
        self.ui.run.clicked.connect(self.run)
        self.ui.back.clicked.connect(self.back_button_clicked)
    def run(self):
        try:
            sentMessage = self.ui.sentMessage.text().encode()
            receivedMessage = self.ui.receivedMessage.text().encode()
            key = self.ui.key.text().encode()
            if not sentMessage:
                raise ValueError("Sent message is empty")
            if not receivedMessage:
                raise ValueError("Received message is empty")
            if not key:
                raise ValueError("Key is empty")
            auth = perform_authentication(sentMessage, receivedMessage)
            if auth:
                self.ui.authOutput.setStyleSheet("color: green; background:white; border-radius: 6px;")
                self.ui.authOutput.setText(str(auth))
            else:
                self.ui.authOutput.setStyleSheet("color: red; background:white; border-radius: 6px;")
                self.ui.authOutput.setText(str(auth))
            conf = confidentiality_authentication(sentMessage, receivedMessage,key)
            if conf:
                self.ui.confidentialityOutput.setStyleSheet("color: green; background:white; border-radius: 6px;")
                self.ui.confidentialityOutput.setText(str(conf))
            else:
                self.ui.confidentialityOutput.setStyleSheet("color: red; background:white; border-radius: 6px;")
                self.ui.confidentialityOutput.setText(str(conf))
        except Exception as e:
            self.ui.confidentialityOutput.setStyleSheet("color: red; background:white; border-radius: 6px;")
            self.ui.confidentialityOutput.setText(f"An error occurred: {e}")
    def clear_inputs(self):
        self.ui.sentMessage.setText("")
        self.ui.receivedMessage.setText("")
        self.ui.key.setText("")
        self.ui.authOutput.setText("")
        self.ui.confidentialityOutput.setText("")
    def back_button_clicked(self):
        self.clear_inputs()
        self.backClicked.emit()
        self.close()

