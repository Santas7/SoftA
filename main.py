from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QGridLayout, QLineEdit, \
    QVBoxLayout, QTextEdit, QProgressBar
from PyQt6 import QtGui, QtWidgets, QtCore
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # settings window MainWindow
        self.setWindowTitle("PCt")
        self.setFixedSize(QSize(380, 500)) # size window
        self.title = QLabel("PCt", self)
        self.setStyleSheet("background-color : black")
        # standart text
        font = QtGui.QFont()
        font.setFamily('CeraPro-Bold')  # font
        font.setPointSize(14)  # size of font

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
