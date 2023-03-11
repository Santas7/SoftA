import os

from PyQt6.QtCore import QSize, QUrl
from PyQt6.QtGui import QDesktopServices
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

        # change icon window
        app_icon = QtGui.QIcon()
        app_icon.addFile('img/logo.png', QtCore.QSize(100, 100))
        app.setWindowIcon(app_icon)

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

        self.combo_box.addItem("♻️🍏CodeRunner-4 for MacOS")
        self.combo_box.addItem("♻️🍏ON1 Photo RAW 2023 for MacOS")
        self.combo_box.addItem("♻️🍏Artstudio Pro for MacOS")
        self.combo_box.addItem("♻️🍏Topaz Photo AI for MacOS")
        self.combo_box.addItem("♻️🍏️MWeb Pro for MacOS")
        self.combo_box.addItem("♻️🍏PDF Reader Pro for MacOS")
        self.combo_box.addItem("♻️🍏Grids - For Instagram")
        self.combo_box.addItem("♻️🍏Microsoft Office 2021 for MacOS")
        self.combo_box.addItem("♻️🍏️DockView for MacOS")
        self.combo_box.addItem("♻️🍏Outline for MacOS")
        self.combo_box.addItem("♻️🍏Keep It for MacOS")
        self.combo_box.addItem("♻️🍏️4K Stogram Pro for MacOS")
        self.combo_box.addItem("♻️🍏️Camera Lock for MacOS")
        self.combo_box.addItem("♻️🍏GarageSale for MacOS")
        self.combo_box.addItem("♻️🍏Microphone Lock for MacOS")
        self.combo_box.addItem("♻️🍏️SQLPro for SQLite MacOS")
        self.combo_box.addItem("♻️🍏Rectangle Pro for MacOS")
        self.combo_box.addItem("♻️🍏Presentation Helper for MacOS")

        self.combo_box.addItem("♻️🪟Microsoft Office 2021 for WindowsOS")
        self.combo_box.addItem("♻️🪟Adobe Photoshop 2023 for WindowsOS")

        self.combo_box.addItem("🕹🍏Superhot: Mind Control Delete for MacOS")
        self.combo_box.addItem("🕹🍏Minecraft Java Edition for MacOS")
        self.combo_box.addItem("🕹🍏Java-8 for MacOS")
        self.combo_box.addItem("🕹🍏Superliminal for MacOS")
        self.combo_box.addItem("🕹🍏GTA: SA for MacOS")
        self.combo_box.addItem("🕹🍏Scythe: Digital Edition for MacOS")
        self.combo_box.addItem("🕹🍏Untitled Goose Game for MacOS")
        self.combo_box.addItem("🕹🍏Mini Metro for MacOS")
        self.combo_box.addItem("🕹🍏Alto's Odyssey: The Lost City for MacOS")
        self.combo_box.addItem("🕹🍏Alto's Adventure for MacOS")
        self.combo_box.addItem("🕹🪟Hogwarts Legacy for WindowsOS")
        self.combo_box.addItem("🕹🪟GTA V for WindowsOS")
        self.combo_box.addItem("🕹🪟Cyberpunk2077 for WindowsOS")
        self.combo_box.move(93, 100)
        self.combo_box.setFixedSize(QSize(200, 40))

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

        elif self.key == 1:
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

        elif self.key == 2:
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
        elif self.key == 3:
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/9JUa-bZct_uDgw"))
        elif self.key == 4:
            QDesktopServices.openUrl(QUrl("https://drive.google.com/file/d/10EnuBBtovTO_TSsJQ_SrXJ0OKmhbUXZ0/view?usp=sharing"))
        elif self.key == 5:
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/naQmxsOFJv2Yrw"))
        elif self.key == 6:
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/WTpmQJxkHmO0BA"))
        elif self.key == 7:
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/W2Ksd02qaZRckA"))
        elif self.key == 8:
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/phpSmax0D7liZg"))
        elif self.key == 9:
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/Muh_WphmiLy7eg"))
        elif self.key == 10:
            QDesktopServices.openUrl(QUrl("https://drive.google.com/file/d/1e0ePKx_e4M8znCwU3YeacqY7YazEy2dC/view?usp=sharing"))
        elif self.key == 11:
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/HXGKt4CVjHcB0g"))
        elif self.key == 12:
            # Outline for MacOS
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/-kAF2wcXzP5oKw"))
        elif self.key == 13:
            # Keep It for MacOS
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/zSDOLQVOFv2amQ"))
        elif self.key == 14:
            # 4K Stogram Pro for MacOS
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/9BRi2wzDh_9xjw"))
        elif self.key == 15:
            # Camera Lock for MacOS
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/43bsBq47OayfPA"))
        elif self.key == 16:
            # GarageSale for MacOS
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/vxyl8HGhjZNeAA"))
        elif self.key == 17:
            # Microphone Lock for MacOS
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/uw3DzUecf_07XA"))
        elif self.key == 18:
            # SQLPro for SQLite MacOS
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/x0mGXZNjKHqMRw"))
        elif self.key == 19:
            # Rectangle Pro for MacOS
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/BKpFIpprwNuHCQ"))
        elif self.key == 20:
            # Presentation Helper for MacOS
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/4wjy-4wR0QPDfQ"))

        elif self.key == 21:
            # office for windows
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/WkZTqe9sc5QQKg"))
        elif self.key == 22:
            # photoshop for windows
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/JwO6TBTBoKgrDA"))

        elif self.key == 23:
            QDesktopServices.openUrl(QUrl("https://drive.google.com/file/d/1hDMrzg0p6wG5jjVkxXkcL8A1RCuaUcxc/view?usp=sharing"))
        elif self.key == 24:
            # minecraft
            QDesktopServices.openUrl(QUrl("https://drive.google.com/file/d/1vgGctLdb5leB1-OXb8YoW32NahAQl81F/view?usp=sharing"))
        elif self.key == 25:
            # java - 8
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/XW7WncxRW_6LSQ"))
        elif self.key == 26:
            # Superliminal for MacOS
            QDesktopServices.openUrl(QUrl("https://drive.google.com/file/d/1vApbfojcnx2-j2cD-s8XTgGbDRyQWiRu/view?usp=sharing"))
        elif self.key == 27: 
            # gta sa
            QDesktopServices.openUrl(QUrl("https://drive.google.com/file/d/1FVNinwsi_j2VKzjTRjPT0NlDY2QtPpdq/view?usp=sharing"))
        elif self.key == 28:
            # Scythe: Digital Edition for MacOS
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/tjex6IF_rp_mwA"))
        elif self.key == 29:
            # Untitled Goose Game for MacOS
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/UMvlfZuYp11NyA"))
        elif self.key == 30:
            # Mini Metro for MacOS
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/NU33DCOyuwPryw"))
        elif self.key == 31:
            # Alto's Odyssey: The Lost City for MacOS
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/otl7DwwC720YPg"))
        elif self.key == 32:
            # Alto's Adventure for MacOS
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/IPDN6KjcITJhlg"))
        elif self.key == 33: #
            # hogwarts-legacy
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/QU3uqtTCzgZTWQ"))
        elif self.key == 34: #
            # gta v for windowsos
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/SYIV9W5XcmszYw"))
        elif self.key == 35: #
            # cyberpunk2077 for windowsos
            QDesktopServices.openUrl(QUrl("https://disk.yandex.ru/d/l0-F-QBxDowXbA"))

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
            self.combo_box.addItem("✅Word(2023)")
            self.combo_box.addItem("✅Excel(2023)")
            self.combo_box.addItem("✅Power-Point(2023)")
            self.combo_box.addItem("✅OneNote(2023)")
            self.combo_box.addItem("✅Outlook(2023)")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
        elif self.key == 3:
            self.combo_box.addItem("✅CodeRunner-4")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)
        elif self.key == 4:
            self.combo_box.addItem("✅ON1 Photo RAW")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)
        elif self.key == 5:
            self.combo_box.addItem("✅Artstudio Pro")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)
        elif self.key == 6:
            self.combo_box.addItem("✅Topaz Photo AI")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)
        elif self.key == 7:
            self.combo_box.addItem("✅MWeb Pro")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)
        elif self.key == 8:
            self.combo_box.addItem("✅PDF Reader Pro")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)

        elif self.key == 9:
            self.combo_box.addItem("✅Grids Instagram")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)
        elif self.key == 10:
            self.combo_box.addItem("✅Microsoft Office 2021")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)
        elif self.key == 11:
            self.combo_box.addItem("✅DockView")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)
        elif self.key == 12: #
            self.combo_box.addItem("✅Outline")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)
        elif self.key == 13: #
            self.combo_box.addItem("✅Keep It")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)
        elif self.key == 14: #
            self.combo_box.addItem("✅4K Stogram Pro")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)

        elif self.key == 15: #
            self.combo_box.addItem("✅Camera Lock")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)
        elif self.key == 16: #
            self.combo_box.addItem("✅GarageSale")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)
        elif self.key == 17: #
            self.combo_box.addItem("✅Microphone Lock")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)
        elif self.key == 18: #
            self.combo_box.addItem("✅SQLPro for SQLite")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)
        elif self.key == 19: #
            self.combo_box.addItem("✅Rectangle Pro")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)
        elif self.key == 20: #
            self.combo_box.addItem("✅Presentation Helper")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)

        elif self.key == 21: #
            self.combo_box.addItem("✅Microsoft Office")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)
        elif self.key == 22: #
            self.combo_box.addItem("✅Adobe Photoshop 2023")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Program")
            self.act.setText("GET")
            self.title.move(90, 50)

        elif self.key == 23:
            self.combo_box.addItem("✅Superhot: Mind Control Delete")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Game")
            self.act.setText("GET")
            self.title.move(110, 50)
        elif self.key == 24:
            self.combo_box.addItem("✅Minecraft")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Game")
            self.act.setText("GET")
            self.title.move(110, 50)
        elif self.key == 25:
            self.combo_box.addItem("✅Java-8")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Game")
            self.act.setText("GET")
            self.title.move(110, 50)
        elif self.key == 26:
            self.combo_box.addItem("✅Superliminal")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Game")
            self.act.setText("GET")
            self.title.move(110, 50)
        elif self.key == 27:
            self.combo_box.addItem("✅GTA: SA")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Game")
            self.act.setText("GET")
            self.title.move(110, 50)
        elif self.key == 28:
            self.combo_box.addItem("✅Scythe: Digital Edition")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Game")
            self.act.setText("GET")
            self.title.move(110, 50)
        elif self.key == 29:
            self.combo_box.addItem("✅Untitled Goose Game")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Game")
            self.act.setText("GET")
            self.title.move(110, 50)
        elif self.key == 30:
            self.combo_box.addItem("✅Mini Metro")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Game")
            self.act.setText("GET")
            self.title.move(110, 50)
        elif self.key == 31:
            self.combo_box.addItem("✅Alto's Odyssey: The Lost City")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Game")
            self.act.setText("GET")
            self.title.move(110, 50)
        elif self.key == 32:
            self.combo_box.addItem("✅Alto's Adventure")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Game")
            self.act.setText("GET")
            self.title.move(110, 50)
        elif self.key == 33:
            self.combo_box.addItem("✅Hogwarts Legacy")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Game")
            self.act.setText("GET")
            self.title.move(110, 50)
        elif self.key == 34:
            self.combo_box.addItem("✅GTA V")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Game")
            self.act.setText("GET")
            self.title.move(110, 50)
        elif self.key == 35:
            self.combo_box.addItem("✅Cyberpunk2077")
            self.combo_box.move(120, 100)
            self.combo_box.setFixedSize(QSize(150, 40))
            self.title.setText("Get Game")
            self.act.setText("GET")
            self.title.move(110, 50)
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
