import sys
import subprocess
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit,QTextEdit,QVBoxLayout, QFileDialog
import os

class OverlayWindow_1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Overlay')
        self.setGeometry(200, 100, 600, 400)#Dimensions of window
        # | Qt.FramelessWindowHint
        self.setWindowFlags(Qt.WindowStaysOnTopHint )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:rgba(0, 0, 0, 0.7);")

#* Adding button1
        self.button1 = QPushButton('Window 2', self)
        self.button1.clicked.connect(self.open_window_2)
        self.button1.setGeometry(80, 100, 200, 60)
        self.button1.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;  /* Green background */
                color: white;               /* White text */
                font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                font-weight: 800;
                border: none;               /* No border */
                padding: 14px 26px;         /* Some padding */
                text-align: center;         /* Centered text */
                text-decoration: none;      /* No underline */
                display: inline-block;      /* Inline-block */
                font-size: 16px;            /* Increase font size */
                margin: 4px 2px;            /* Some margin */
                transition-duration: 0.4s;  /* 0.4 seconds transition effect */
                cursor: pointer;            /* Pointer/hand icon */
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: white;    /* White background on hover */
                color: black;               /* Black text on hover */
                border: 2px solid #4CAF50;  /* Green border on hover */
            }
        """)

#* Adding button2 for screenshot
        self.button2 = QPushButton('Take Screenshot', self)
        self.button2.setGeometry(80, 100, 200, 60)
        self.button2.move(300, 100)
        self.button2.clicked.connect(self.schedule_screenshot)
        self.button2.setStyleSheet("""
            QPushButton {
                background-color: #f44336;  /* Red background */
                color: white;               /* White text */
                font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                font-weight: 800;
                border: none;               /* No border */
                padding: 14px 26px;         /* Some padding */
                text-align: center;         /* Centered text */
                text-decoration: none;      /* No underline */
                display: inline-block;      /* Inline-block */
                font-size: 16px;            /* Increase font size */
                margin: 4px 2px;            /* Some margin */
                transition-duration: 0.4s;  /* 0.4 seconds transition effect */
                cursor: pointer;            /* Pointer/hand icon */
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: white;    /* White background on hover */
                color: black;               /* Black text on hover */
                border: 2px solid #f44336;  /* Red border on hover */
            }
        """)

#* Adding a textBox
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Enter text here...")
        self.textbox.setGeometry(50, 30, 300, 50)
        self.textbox.setStyleSheet("""
            QLineEdit {
                background-color: rgba(255, 255, 255, 0.7); /* Slightly transparent white background */
                font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                font-weight: 600;
                color: black;                               /* Black text */
                padding: 10px;                              /* Some padding */
                border: 2px solid #cccccc;                  /* Gray border */
                border-radius: 10px;                        /* Rounded corners */
                font-size: 16px;                            /* Increase font size */
            }
            QLineEdit:focus {
                border: 2px solid #4CAF50;  /* Green border on focus */
            }
        """)

#* Button-3 to enter and store the text into the a .txt file
        self.button3 = QPushButton('Enter', self)
        self.button3.setGeometry(400, 15, 100, 40)
        self.button3.clicked.connect(self.save_input)
        self.button3.setStyleSheet("""
            QPushButton {
                background-color: #f44336;  /* Red background */
                color: white;               /* White text */
                font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                font-weight: 800;
                border: none;               /* No border */
                text-align: center;         /* Centered text */
                text-decoration: none;      /* No underline */
                display: inline-block;      /* Inline-block */
                font-size: 16px;            /* Increase font size */
                margin: 4px 2px;            /* Some margin */
                transition-duration: 0.4s;  /* 0.4 seconds transition effect */
                cursor: pointer;            /* Pointer/hand icon */
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: white;    /* White background on hover */
                color: black;               /* Black text on hover */
                border: 2px solid #f44336;  /* Red border on hover */
            }
        """)

#* Button-4 to clear the textbox
        self.button4 = QPushButton('Clear', self)
        self.button4.setGeometry(400, 55, 100, 40)
        self.button4.clicked.connect(self.clear_input)
        self.button4.setStyleSheet("""
            QPushButton {
                background-color: #bdbdbd;  /* Red background */
                color: white;               /* White text */
                font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                font-weight: 800;
                border: none;               /* No border */
                text-align: center;         /* Centered text */
                text-decoration: none;      /* No underline */
                display: inline-block;      /* Inline-block */
                font-size: 16px;            /* Increase font size */
                margin: 4px 2px;            /* Some margin */
                transition-duration: 0.4s;  /* 0.4 seconds transition effect */
                cursor: pointer;            /* Pointer/hand icon */
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: white;    /* White background on hover */
                color: black;               /* Black text on hover */
                border: 2px solid #f44336;  /* Red border on hover */
            }
        """)
#* Button-5 to run the script for the GPT (To be combined with run screenshots)
        self.button5 = QPushButton('Run GPT', self)
        self.button5.setGeometry(400, 155, 100, 40)
        self.button5.clicked.connect(self.run_script)
        self.button5.setStyleSheet("""
            QPushButton {
                background-color: #bdbdbd;  /* Red background */
                color: white;               /* White text */
                font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                font-weight: 800;
                border: none;               /* No border */
                text-align: center;         /* Centered text */
                text-decoration: none;      /* No underline */
                display: inline-block;      /* Inline-block */
                font-size: 16px;            /* Increase font size */
                margin: 4px 2px;            /* Some margin */
                transition-duration: 0.4s;  /* 0.4 seconds transition effect */
                cursor: pointer;            /* Pointer/hand icon */
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: white;    /* White background on hover */
                color: black;               /* Black text on hover */
                border: 2px solid #f44336;  /* Red border on hover */
            }
        """)



#!Saving Textbox input
    def save_input(self):
        Text_Folder = "User_Inputs"
        file_path = os.path.join(Text_Folder, "user_Input.txt")

        user_input = self.textbox.text()
        print(f"User input: {user_input} saved")  # Printing input in the terminal

        with open(file_path, "a") as file:  # Saving the file
            file.write(user_input + "\n")

        self.textbox.clear()
    
#!Clearing the input in the textbox
    def clear_input(self):
        self.textbox.clear()

#!Adding a fxn to delay the input
    def schedule_screenshot(self):
        QTimer.singleShot(1000, self.prepare_screenshot)

#!Hiding the window for screenshot( 1.5s )
    def prepare_screenshot(self):
        # Hide the entire window before taking the screenshot
        self.hide()
        QTimer.singleShot(1500, self.take_screenshot)

#!Taking screenshots 
    def take_screenshot(self):
        screenshot_folder = "User_Inputs"
        screen = QApplication.primaryScreen()
        screenshot = screen.grabWindow(0)

        file_name = "screenshot_.png"
        file_path = os.path.join(screenshot_folder, file_name)
        screenshot.save(file_path, 'png')
        print(f"Screenshot saved to {file_path}")

        self.show() #Show the window again

#!Colors of the window
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(0, 0, 0, 120))  # Changing the color of bg window
        painter.drawRect(self.rect())

#!Linked script to run 
    def run_script(self):
        script_path = os.path.join(os.path.dirname(__file__), 'main_1_docs.py')
        subprocess.run(['python', script_path])
#!Fxn to open Window-2
    def open_window_2(self):
        self.window2 = OverlayWindow_2()  # Create an instance of Window2
        self.window2.show()
        self.hide()


#!Defining another class to execute it upon a button click

class OverlayWindow_2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Overlay')
        self.setGeometry(500, 300, 600, 300)
        # |Qt.FramelessWindowHint
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:rgba(0, 0, 0, 0.7);")
        self.setWindowTitle("Window 2")
        # Add any other widgets or functionality for Window2 here

#!Adding a button to go back to previous window

#*Adding button1
        self.button1 = QPushButton('Window 1', self)
        self.button1.clicked.connect(self.open_window_1)
        self.button1.setGeometry(400, 40, 200, 60)
        self.button1.setStyleSheet("""
            QPushButton {
                background-color: #795dec;  /* Green background */
                color: white;               /* White text */
                font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                font-weight: 800;
                border: none;               /* No border */
                padding: 14px 26px;         /* Some padding */
                text-align: center;         /* Centered text */
                text-decoration: none;      /* No underline */
                display: inline-block;      /* Inline-block */
                font-size: 16px;            /* Increase font size */
                margin: 4px 2px;            /* Some margin */
                transition-duration: 0.4s;  /* 0.4 seconds transition effect */
                cursor: pointer;            /* Pointer/hand icon */
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: white;    /* White background on hover */
                color: black;               /* Black text on hover */
                border: 2px solid #795dec;  /* Green border on hover */
            }
        """)
    #*Adding textbox-2 to display text 
        vbox = QVBoxLayout()
        self.text_edit = QTextEdit(self)
        # self.textbox = QLineEdit(self)
        self.text_edit.isReadOnly()
        self.text_edit.setText('Initial Text')
        vbox.addWidget(self.text_edit)
        self.setLayout(vbox)
        self.text_edit.setGeometry(50, 30, 300, 100)
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: rgba(255, 255, 255, 0.7); /* Slightly transparent white background */
                font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                font-weight: 600;
                color: #008f11;
                background-color: #0D0208;  
                padding: 10px;                              /* Some padding */
                border: 2px solid #cccccc;                  /* Gray border */
                border-radius: 10px;                        /* Rounded corners */
                font-size: 16px;                            /* Increase font size */
            }
            QLineEdit:focus {
                border: 2px solid #4CAF50;  /* Green border on focus */
            }
        """)
    #!Colors of the window
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(0, 0, 0, 120))  # Changing the color of bg window
        painter.drawRect(self.rect())

        self.show()
 
#!Function to shift back to window-1
    def open_window_1(self):
        self.window1 = OverlayWindow_1()  # Create an instance of Window2
        self.window1.show()
        self.hide()

#!Showing the final window
if __name__ == '__main__':
    app = QApplication(sys.argv)
    overlay = OverlayWindow_1()
    overlay.show()
    sys.exit(app.exec_())
    
    """ Output textbox : Window 2 """

    