from PySide6 import QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QWidget
from ui_CryptoMain import Ui_CryptoMain
from aesMain import AES_Widget
from AuthMain import AUTH_Widget
import sys, os

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class CryptoKit(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CryptoMain()
        self.ui.setupUi(self)
        self.setWindowTitle("CryptoKit")
        self.setFixedSize(self.size())
        self.ui.next.clicked.connect(self.next_button_clicked)
    def next_button_clicked(self):
        if self.ui.AESChoice.isChecked():
            self.aes_widget = AES_Widget()
            self.aes_widget.backClicked.connect(self.show)
            self.aes_widget.show()
            self.close()
        elif self.ui.AUTHChoice.isChecked():
            self.auth_widget = AUTH_Widget()
            self.auth_widget.backClicked.connect(self.show)
            self.auth_widget.show()
            self.close()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir, 'icon.ico')))
    widget = CryptoKit()
    widget.show()
    app.exec()