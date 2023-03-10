import os

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QGridLayout, QLineEdit, \
    QVBoxLayout, QTextEdit, QProgressBar, QComboBox, QMessageBox
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
        self.combo_box.addItem("💻MacOS and UnixOS")
        self.combo_box.addItem("💻Microsoft Office")
        self.combo_box.move(120, 100)
        self.combo_box.setFixedSize(QSize(150, 40))

        self.continu = QPushButton("CONTINUE", self)
        self.continu.setFixedSize(QSize(150, 50))
        self.continu.move(120, 150)
        self.continu.setFont(font)
        self.continu.setStyleSheet("background-color : #FFA07A")
        self.config = 0

        # Connect the signal to the slot
        self.combo_box.activated.connect(self.on_combo_box_changed)

        self.continu.clicked.connect(self.next)
        self.show()

    def on_combo_box_changed(self, text):
        self.config = text
        print(self.config)

    def next(self):
        window_ = NewWindow(self.config)
        window_.setStyleSheet("""
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
        self.act.setFixedSize(QSize(160, 50))
        self.act.move(115, 150)
        self.act.setFont(font)
        self.act.setStyleSheet("background-color : #FFA07A")

        # Create a combo box and add items
        self.combo_box = QComboBox(self)
        self.check_key()
        self.combo_box.activated.connect(self.on_combo_box_changed)
        self.key2 = 0
        self.act.clicked.connect(self.cho)
        self.show()

    def on_combo_box_changed(self, text):
        self.key2 = text

    def get_key(self):
        if self.key2 == 2:
            return "W269N-WFGWX-YVC9B-4J6C9-T83GX"
        elif self.key2 == 1:
            return "FJ82H-XT6CR-J8D7P-XQJJ2-GPDD4"
        elif self.key2 == 3:
            return "XCVCF-2NXM9-723PB-MHCB7-2RYQQ"
        elif self.key2 == 4:
            return 0
        elif self.key2 == 5:
            return "VDYBN-27WPP-V4HQT-9VMD4-VMK7H"

    def cho(self):
        if self.key == 0:
            if self.key2 == 0:
                # 12 windows
                print("This package is not yet available!")

            elif self.key2 == 1:
                # 11 windows
                os.system("slmgr /dli")
                os.system("slmgr /ipk " + self.get_key())
                os.system("slmgr /skms kms.digiboy.ir")
                os.system("slmgr /ato")
            elif self.key2 == 2:
                # 10 windows
                os.system("slmgr.vbs /upk")
                os.system("slmgr.vbs /ipk " + self.get_key())
                os.system("slmgr /skms kms.digiboy.ir")
                os.system("slmgr.vbs /ato")
            elif self.key2 == 3:
                # 8 windows
                os.system("slmgr /upk")
                os.system("slmgr /ipk " + self.get_key())
                os.system("slmgr / skms kms8.msguides.com")
                os.system("slmgr.vbs /ato")
            elif self.key2 == 4:
                # 7 windows
                os.system("slmgr /rearm")
            elif self.key2 == 5:
                # Server-standart windows
                os.system("slmgr /ipk " + self.get_key())
                os.system("slmgr /skms kms.digiboy.ir")
                os.system("slmgr /ato")
            elif self.key2 == 6:
                # xp windows
                os.system("cd windows/system32/oobe/msoobe/a")
            elif self.key2 == 7:
                # 98 windows
                os.system("cd windows/system32/oobe/msoobe/a")
            elif self.key2 == 8:
                # 95 windows
                os.system("cd windows/system32/oobe/msoobe/a")

        if self.key == 1:
            if self.key2 == 0:
                # catalina
                print("You may have already activated this package before!")
            elif self.key2 == 1:
                # Mojave
                print("You may have already activated this package before!")
            elif self.key2 == 2:
                #  High Sierra
                print("You may have already activated this package before!")
            elif self.key2 == 3:
                # Sierra
                print("You may have already activated this package before!")
            elif self.key2 == 4:
                # Monterey
                print("You may have already activated this package before!")
            elif self.key2 == 5:
                # Big Sur
                print("You may have already activated this package before!")
            elif self.key2 == 6:
                # ubuntu
                print("You may have already activated this package before!")

        if self.key == 2:
            if self.key2 == 0:
                # word
                print("You may have already activated this package before!")
            elif self.key2 == 1:
                # excel
                print("You may have already activated this package before!")
            elif self.key2 == 2:
                #  power-point
                print("You may have already activated this package before!")
            elif self.key2 == 3:
                # onenote
                print("You may have already activated this package before!")
            elif self.key2 == 4:
                # outlook
                print("You may have already activated this package before!")


    def check_key(self):
        if self.key == 0:
            self.combo_box.addItem("❌Window-12")
            self.combo_box.addItem("✅Windows-11")
            self.combo_box.addItem("✅Windows-10")
            self.combo_box.addItem("✅Window-8")
            self.combo_box.addItem("✅Windows-7")
            self.combo_box.addItem("✅Windows-Server")
            self.combo_box.addItem("⚠️Windows-XP")
            self.combo_box.addItem("⚠️Windows-98")
            self.combo_box.addItem("⚠️Windows-95")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
        elif self.key == 1:
            self.combo_box.addItem("✅MacOS Catalina")
            self.combo_box.addItem("✅MacOS Mojave")
            self.combo_box.addItem("⚠️MacOS High Sierra")
            self.combo_box.addItem("✅MacOS Sierra")
            self.combo_box.addItem("✅MacOS Monterey")
            self.combo_box.addItem("⚠️MacOS Big Sur")
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
