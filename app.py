from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from module1 import *
import sys
import os
import pkgutil


if getattr(sys, 'frozen',  False):
    print('run in a bundle')
else:
    print('run live')

text_txt = pkgutil.get_data( 'data', 'text.txt' )


class Main(QMainWindow):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.line = QLineEdit(self)
        print(b)
        text = text_txt.decode('utf-8')
        self.line.setText(text)
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    main = Main()
    app.exec_()