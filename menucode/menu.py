import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton,  QLineEdit
from PyQt6.QtCore import QUrl, pyqtSignal
from PyQt6.QtGui import QDesktopServices
from main.chap1 import Chap1Window

class Menu_window(QWidget):
    switch_window = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.setWindowTitle("menu")
        self.setFixedSize(600,600)

        self.bugbutton = QPushButton(self)
        self.bugbutton.setText("bug report")
        self.bugbutton.setGeometry(100, 200, 80, 50)
        self.bugbutton.clicked.connect(self.bug_report_open)

        self.open_button = QPushButton(self)
        self.open_button.setText("music credit")
        self.open_button.setGeometry(100, 400, 80, 50)
        self.open_button.clicked.connect(self.open_music_credit)

        self.creditbutton = QPushButton(self)
        self.creditbutton.setText("credit")
        self.creditbutton.setGeometry(400, 200, 50, 50)
        self.creditbutton.clicked.connect(self.creditopen)

        self.link_label = QLabel(self)
        self.link_label.setText('"https://github.com/jinya11/final-myproject"')
        self.link_label.setGeometry(300, 550, 500, 50)

        self.open_link_button = QPushButton('Open Link', self)
        self.open_link_button.clicked.connect(self.open_link)
        self.open_link_button.setGeometry(400, 400, 70, 50)

        self.end_button = QPushButton(self)
        self.end_button.setText("End")
        self.end_button.setGeometry(280, 100, 50, 50)
        self.end_button.clicked.connect(self.go_backmain_to_chap1)

    def go_backmain_to_chap1(self):
        self.switch_window.emit()
        self.close()

    def open_link(self):
            url = self.link_label.text().strip('"')
            QDesktopServices.openUrl(QUrl(url))

    def creditopen(self):
        from main.chap1 import creditWindow
        self.creditopen = creditWindow()
        self.creditopen.show()

    def open_music_credit(self):
        from main.chap1 import Music_credit
        self.music_credit = Music_credit()
        self.music_credit.show()


    def bug_report_open(self):
        from main.chap1 import BugreportWindow
        self.bug_report_open = BugreportWindow()
        self.bug_report_open.show()


def exception_hook(except_type, value, traceback):
    print(except_type, value, traceback)
    print(traceback.format_exc())
    exit(1)

if __name__ == '__main__':
    sys.excepthook = exception_hook
    qapp = QApplication(sys.argv)

    menu_window = Menu_window()
    chap1_window = Chap1Window()

    menu_window.switch_window.connect(chap1_window.show)
    chap1_window.switch_window.connect(menu_window.show)

    input_window = Menu_window()
    input_window.show()
    sys.exit(qapp.exec())