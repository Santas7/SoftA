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
        print(self.config)

    def next(self):
        window_ = NewWindow(self.config)
        window_.exec()

class NewWindow(QtWidgets.QDialog):
    def __init__(self, key):
        super().__init__()
        self.key = key
        self.setWindowTitle("SoftA | SettingUp")
        self.setFixedSize(QSize(380, 500))
        self.title = QLabel("Activation Process", self)
        font = QtGui.QFont()
        font.setFamily('CeraPro-Bold')  # сам шрифт
        font.setPointSize(14)  # размер шрифта
        # standart text
        font = QtGui.QFont()
        font.setFamily('CeraPro-Bold')  # font
        font.setPointSize(14)  # size of font

        # title text
        font_ = QtGui.QFont()
        font_.setFamily('CeraPro-Bold')  # font
        font_.setPointSize(27)  # size of font
        self.title.setFont(font_)
        self.title.move(50, 50)
        self.act = QPushButton("ACTIVATION", self)
        self.act.setFixedSize(QSize(150, 50))
        self.act.move(120, 150)
        self.act.setFont(font)
        self.act.setStyleSheet("background-color : #FFA07A")

        # Create a combo box and add items
        self.combo_box = QComboBox(self)
        self.check_key()

        self.show()

    def check_key(self):
        if self.key == 0:
            self.combo_box.addItem("✅Window-12")
            self.combo_box.addItem("✅Windows-11")
            self.combo_box.addItem("✅Windows-10")
            self.combo_box.addItem("✅Window-8")
            self.combo_box.addItem("✅Windows-7")
            self.combo_box.addItem("✅Windows-Server")
            self.combo_box.addItem("✅Windows-XP")
            self.combo_box.addItem("✅Windows-98")
            self.combo_box.addItem("✅Windows-95")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
        elif self.key == 1:
            self.combo_box.addItem("✅MacOS Catalina")
            self.combo_box.addItem("✅MacOS Mojave")
            self.combo_box.addItem("✅MacOS High Sierra")
            self.combo_box.addItem("✅MacOS Sierra")
            self.combo_box.addItem("✅MacOS Monterey")
            self.combo_box.addItem("✅MacOS Big Sur")
            self.combo_box.addItem("✅Linux Ubuntu(FREE)")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
        elif self.key == 2:
            self.combo_box.addItem("✅Word(2022)")
            self.combo_box.addItem("✅Excel(2022)")
            self.combo_box.addItem("✅Power-Point(2022)")
            self.combo_box.addItem("✅OneNote(2022)")
            self.combo_box.addItem("✅Outlook(2022)")
            self.combo_box.addItem("✅Word(2019)")
            self.combo_box.addItem("✅Excel(2019)")
            self.combo_box.addItem("✅Power-Point(2019)")
            self.combo_box.addItem("✅Word(2018)")
            self.combo_box.addItem("✅Excel(2018)")
            self.combo_box.addItem("✅Power-Point(2018)")
            self.combo_box.addItem("✅Word(2016)")
            self.combo_box.addItem("✅Excel(2016)")
            self.combo_box.addItem("✅Power-Point(2016)")
            self.combo_box.addItem("✅Word(2008)")
            self.combo_box.addItem("✅Excel(2008)")
            self.combo_box.addItem("✅Power-Point(2008)")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
        else:
            print("error!\n")

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
