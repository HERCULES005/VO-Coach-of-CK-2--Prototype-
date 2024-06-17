from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
import os
import sys

class OverlayWindow_2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_from_file_2 = True  # Initial state: load from file 2
        self.load_text()

    def initUI(self):
        self.setWindowTitle('Overlay')
        self.setGeometry(200, 100, 600, 600)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:rgba(0, 0, 0, 0.7);")
        self.setWindowTitle("Window 2")

        vbox = QVBoxLayout()
        self.textbox_2 = QTextEdit(self)
        self.textbox_2.setReadOnly(True)
        self.textbox_2.setText('Initial Text')
        vbox.addWidget(self.textbox_2)
        self.setLayout(vbox)
        self.textbox_2.setGeometry(30, 15, 360, 360)
        self.textbox_2.setStyleSheet("""
            QTextEdit {
                background-color: rgba(255, 255, 255, 0.7);
                font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                font-weight: 600;
                color: #008f11;
                background-color: #0D0208;  
                padding: 10px;
                border: 2px solid #cccccc;
                border-radius: 10px;
                font-size: 16px;
            }
        """)

        self.button_switch = QPushButton('Switch File', self)
        self.button_switch.clicked.connect(self.switch_file)
        self.button_switch.setGeometry(400, 40, 200, 60)
        self.button_switch.setStyleSheet("""
            QPushButton {
                background-color: #795dec;
                color: white;
                font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                font-weight: 800;
                border: none;
                padding: 14px 26px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                margin: 4px 2px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: white;
                color: black;
                border: 2px solid #795dec;
            }
        """)
        
        # Other buttons...

        self.button5 = QPushButton('Quit', self)
        self.button5.clicked.connect(self.exit_window)
        self.button5.setGeometry(400, 360, 200, 60)
        self.button5.setStyleSheet("""
            QPushButton {
                background-color: #800000;
                color: white;
                font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                font-weight: 800;
                border: none;
                padding: 14px 26px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                margin: 4px 2px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: black;
                color: red;
                border: 2px solid red;
            }
        """)

    def exit_window(self):
        sys.exit(app.exec_())

    def load_text_from_file(self):
        Text_Folder = "./"
        file_path = os.path.join(Text_Folder, "output.txt")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                content = file.read()
                self.textbox_2.setText(content)
        else:
            self.textbox_2.setText("No input file found.")

    def load_text_from_file_2(self):
        Text_Folder = "./"
        file_path = os.path.join(Text_Folder, "output_Assistant.txt")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                content = file.read()
                self.textbox_2.setText(content)
        else:
            self.textbox_2.setText("No input file found.")

    def switch_file(self):
        self.load_from_file_2 = not self.load_from_file_2
        self.load_text()

    def load_text(self):
        if self.load_from_file_2:
            self.load_text_from_file_2()
        else:
            self.load_text_from_file()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(0, 0, 0, 120))
        painter.drawRect(self.rect())

        self.show()

    def open_window_1(self):
        self.window1 = OverlayWindow_1()
        self.window1.show()
        self.hide()

    def clear_input(self):
        self.textbox_2.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    overlay = OverlayWindow_2()
    overlay.show()
    sys.exit(app.exec_())
