from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QGridLayout, QLineEdit, \
    QVBoxLayout, QTextEdit, QProgressBar, QComboBox
from PyQt6 import QtGui, QtWidgets, QtCore
import sys
import config

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # settings window MainWindow
        self.setWindowTitle("SoftA")
        self.setFixedSize(QSize(380, 500)) # size window
        self.title = QLabel("SoftA", self)

        # standart text
        font = QtGui.QFont()
        font.setFamily('CeraPro-Bold')  # font
        font.setPointSize(14)  # size of font

        # title text
        font_ = QtGui.QFont()
        font_.setFamily('CeraPro-Bold')  # font
        font_.setPointSize(27)  # size of font

        # change for title
        self.title.setFont(font_)
        self.title.move(150, 50)

        # Create a combo box and add items
        self.combo_box = QComboBox(self)
        self.combo_box.addItem("💻WindowsOS")
        self.combo_box.addItem("💻UnixOS")
        self.combo_box.addItem("💻Microsoft Office")
        self.combo_box.move(120, 100)
        self.combo_box.setFixedSize(QSize(150, 40))

        self.continu = QPushButton("CONTINUE", self)
        self.continu.setFixedSize(QSize(150, 50))
        self.continu.move(120, 150)
        self.continu.setFont(font)
        self.continu.setStyleSheet("background-color : #FFA07A")
        self.config = None

        # Connect the signal to the slot
        self.combo_box.activated.connect(self.on_combo_box_changed)

        self.continu.clicked.connect(self.next)
        self.show()

    def on_combo_box_changed(self, text):
        self.config = text

    def next(self):
        window_ = NewWindow()
        window_.exec()

class NewWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SoftA | SettingUp")
        self.setFixedSize(QSize(380, 500))
        self.label = QLabel("", self)
        font = QtGui.QFont()
        font.setFamily('CeraPro-Bold')  # сам шрифт
        font.setPointSize(14)  # размер шрифта
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet("""
        QPushButton {
            border-radius: 15px;
            background-color: #FFA07A;
            color: white;
            font-size: 20px;
            padding: 10px 20px;
        }

        QPushButton:hover {
            background-color: #FF7F50;
        }

        QPushButton:pressed {
            background-color: #FF7F50;
        }
    """)
    app.exec()
