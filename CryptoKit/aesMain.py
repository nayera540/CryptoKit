import binascii

from PySide6 import QtGui
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget
import os
from ui_AES import Ui_AES
from AES import encrypt_aes, decrypt_aes

basedir = os.path.dirname(__file__)
class AES_Widget(QWidget):
    backClicked = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_AES()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'icon.ico')))
        self.setWindowTitle("CryptoKit-AES")
        self.setFixedSize(self.size())
        self.ui.enc.clicked.connect(self.encrypt)
        self.ui.dec.clicked.connect(self.decrypt)
        self.ui.save.clicked.connect(self.save_to_file)
        self.ui.back.clicked.connect(self.back_button_clicked)
        self.ciphertext = None

    def encrypt(self):
        try:
            path = self.ui.filePath.text()
            mode = self.ui.modeOptions.currentText()
            key = self.ui.key.text().encode()
            iv = self.ui.initVector.text().encode()
            with open(path, 'rb') as f:
                plaintext = f.read()
            if not plaintext:
                raise ValueError("File is empty")
            self.ciphertext = encrypt_aes(key, plaintext, mode, iv)
            self.ui.output.setText("AES Encrypted Output")
            self.ui.outputText.setStyleSheet("color: black; background:white; border-radius: 6px;")
            self.ui.outputText.setText(self.ciphertext.hex())
        except Exception as e:
            self.ui.outputText.setStyleSheet("color: red; background:white; border-radius: 6px;")
            self.ui.outputText.setText(f"An error occurred: {e}")

    def decrypt(self):
        try:
            self.ui.save.setEnabled(False)
            path = self.ui.filePath.text()
            mode = self.ui.modeOptions.currentText()
            key = self.ui.key.text().encode()
            iv = self.ui.initVector.text().encode()
            with open(path, 'r') as f:  # Open the file in text mode
                hex_ciphertext = f.read()

            if not hex_ciphertext:
                raise ValueError("File is empty")

            ciphertext = binascii.unhexlify(hex_ciphertext)  # Convert hex to bytes

            decrypted_message = decrypt_aes(key, ciphertext, mode, iv)

            self.ui.output.setText("AES Decrypted Output")
            self.ui.outputText.setStyleSheet("color: black; background:white; border-radius: 6px;")
            self.ui.outputText.setText(decrypted_message.decode("utf-8"))
        except Exception as e:
            self.ui.outputText.setStyleSheet("color: red; background:white; border-radius: 6px;")
            self.ui.outputText.setText(f"An error occurred: {e}")
        finally:
            self.ui.save.setEnabled(True)

    def save_to_file(self):
        if self.ciphertext is not None:
            with open('decryptedFile.txt', 'w') as f:  # Open the file in text mode
                f.write(self.ciphertext.hex())
    def clear_input(self):
        self.ui.filePath.setText("")
        self.ui.key.setText("")
        self.ui.initVector.setText("")
        self.ui.outputText.setText("")
    def back_button_clicked(self):
        self.clear_input()
        self.backClicked.emit()
        self.close()
