import sys
import subprocess
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QTextEdit, QVBoxLayout, QFileDialog,QListWidget
import os




class OverlayWindow_0(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        # self.load_text_from_file()  # Load text when initializing of sss
        # self.load_text_from_file_2()

    def initUI(self):
        self.setWindowTitle('Overlay')
        self.setGeometry(200, 100, 300, 300)
        # |Qt.FramelessWindowHint
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:rgba(0, 0, 0, 0.7);")
        self.setWindowTitle("Window 2")

#!Adding a button to go to next window

#*Adding button1
        self.button1 = QPushButton('Enter custom query', self) #Takes the user to next window
        # self.button1.clicked.connect(self.open_window_1 )
        self.button1.setGeometry(10, 40, 280, 60)
        self.button1.setStyleSheet("""
            QPushButton {
                background-color: #3537b4;  /* Green background */
                color: white;               /* White text */
                font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                font-weight: 800;
                border: none;               /* No border */
                padding: 14px 26px;         /* Some padding */
                text-align: center;         /* Centered text */
                text-decoration: none;      /* No underline */
                font-size: 16px;            /* Increase font size */
                margin: 4px 2px;            /* Some margin */
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: white;    /* White background on hover */
                color: black;               /* Black text on hover */
                border: 2px solid #795dec;  /* Green border on hover */
            }
        """)



#*Adding button2
        self.button2 = QPushButton('Provide SSS', self)
        # self.button2.clicked.connect(self.open_window_1)
        self.button2.setGeometry(10, 150, 280, 60)
        self.button2.setStyleSheet("""
            QPushButton {
                background-color: #b841c1;  /* Green background */
                color: white;               /* White text */
                font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                font-weight: 800;
                border: none;               /* No border */
                padding: 14px 26px;         /* Some padding */
                text-align: center;         /* Centered text */
                text-decoration: none;      /* No underline */
                font-size: 16px;            /* Increase font size */
                margin: 4px 2px;            /* Some margin */
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: white;    /* White background on hover */
                color: black;               /* Black text on hover */
                border: 2px solid #795dec;  /* Green border on hover */
            }
        """)

#*Adding button3 for exiting the window
        self.button3 = QPushButton('Quit', self)
        self.button3.clicked.connect(self.exit_window)
        self.button3.setGeometry(10, 240, 280, 60)
        self.button3.setStyleSheet("""
            QPushButton {
                background-color: #800000;  /* Green background */
                color: white;               /* White text */
                font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                font-weight: 800;
                border: none;               /* No border */
                padding: 14px 26px;         /* Some padding */
                text-align: center;         /* Centered text */
                text-decoration: none;      /* No underline */
                font-size: 16px;            /* Increase font size */
                margin: 4px 2px;            /* Some margin */
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: black;    /* White background on hover */
                color: red;               /* Black text on hover */
                border: 2px solid red;  /* Green border on hover */
            }
        """)




#!Function to quit the window
    def exit_window(self):
        sys.exit(app.exec_())

#!Function to load output in the Window-2 textbox
    # def load_text_from_file(self):
    #     Text_Folder = "./"
    #     file_path = os.path.join(Text_Folder, "output.txt")

    #     if os.path.exists(file_path):
    #         with open(file_path, "r") as file:
    #             content = file.read()
    #             self.textbox_2.setText(content)
    #     else:
    #         self.textbox_2.setText("No input file found.")

#!Function to load output in the Window-2 textbox
    # def load_text_from_file_2(self):
    #     Text_Folder = "./"
    #     file_path = os.path.join(Text_Folder, "output_Assistant.txt")

    #     if os.path.exists(file_path):
    #         with open(file_path, "r") as file:
    #             content = file.read()
    #             self.textbox_2.setText(content)
    #     else:
    #         self.textbox_2.setText("No input file found.")

    
#!Colors of the window
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(0, 0, 0, 120))  # Changing the color of bg window
        painter.drawRect(self.rect())

        self.show()
 
#! Function to open Overlay_window_1
    # def open_window_1(self):
    #     self.window2 = OverlayWindow_1()  # Create an instance of Window2
    #     self.window2.show()
    #     self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    overlay = OverlayWindow_0()
    overlay.show()
    sys.exit(app.exec_())