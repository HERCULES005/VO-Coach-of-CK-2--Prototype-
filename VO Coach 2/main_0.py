import sys
import subprocess
from PyQt5.QtCore import Qt, QTimer,QPoint
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QTextEdit, QVBoxLayout, QFileDialog,QListWidget,QWidget
import os

class MinimizedWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setWindowFlags( Qt.Tool| Qt.FramelessWindowHint)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool| Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(70, 50)
        self.start_position = QPoint()

#!Function to add the bg color of the window
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(0, 100, 100, 200))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(self.rect())

    def mousePressEvent(self, event):
        self.start_position = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = event.globalPos() - self.start_position
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.start_position = event.globalPos()

    def mouseDoubleClickEvent(self, event):
        self.parent().restore_main_window()

#!-------------------------------------------------------------------------------OVERLAY WINDOW-0 -------------------------------------------------------------------------------!#
#!-------------------------------------------------------------------------------OVERLAY WINDOW-0 -------------------------------------------------------------------------------!#
#!-------------------------------------------------------------------------------OVERLAY WINDOW-0 -------------------------------------------------------------------------------!#


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
        # self.setWindowFlags(Qt.WindowStaysOnTopHint )
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:rgba(0, 0, 0, 0.7);")
        self.setWindowTitle("Window 2")

#* Button to enter custom query
        self.button1 = QPushButton('Enter custom query', self)
        self.button1.clicked.connect(self.open_window_1)
        self.button1.setGeometry(10, 60, 280, 60)
        self.button1.setStyleSheet("""
            QPushButton {
                background-color: #3537b4;  
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


#* Button to Provide sss
        self.button2 = QPushButton('Provide SSS', self)
        self.button2.clicked.connect(self.schedule_screenshot)
        self.button2.setGeometry(10, 150, 280, 60)
        self.button2.setStyleSheet("""
            QPushButton {
                background-color: #b841c1;  
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

#* Button to exit the window
        self.button3 = QPushButton('Quit', self)
        self.button3.clicked.connect(self.exit_window)
        self.button3.setGeometry(10, 220, 280, 60)
        self.button3.setStyleSheet("""
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

#*Button to minimize the window
        self.minimize_button = QPushButton('Mini', self)
        self.minimize_button.clicked.connect(self.minimize_to_widget)
        self.minimize_button.setGeometry(10, 10, 80, 50)
        self.minimize_button.setStyleSheet("""
            QPushButton {
                background-color: gold;  /* Green background */
                color: magenta;               /* White text */
                font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                font-weight: 800;
                border: none;               /* No border */
                padding: 10px;              /* Some padding */
                text-align: center;         /* Centered text */
                text-decoration: none;      /* No underline */
                font-size: 16px;            /* Increase font size */
                margin: 4px 2px;            /* Some margin */
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: white;    /* White background on hover */
                color: black;               /* Black text on hover */
                border: 2px solid #4CAF50;  /* Green border on hover */
            }
        """)

        self.minimized_widget = MinimizedWidget(self)
        self.minimized_widget.hide()

#!Function to minimize to widget
    def minimize_to_widget(self):
        self.hide()
        self.minimized_widget.move(self.frameGeometry().topLeft())
        self.minimized_widget.show()

#?Function to take screenshot and switch to window 1
    def ss_and_switchWindow(self):
        self.schedule_screenshot()
        self.open_window_1()

#?Adding a fxn to delay the input
    def schedule_screenshot(self):
        QTimer.singleShot(1000, self.prepare_screenshot)

#?Hiding the window for screenshot( 1.5s )
    def prepare_screenshot(self):
        # Hide the entire window before taking the screenshot
        self.hide()
        QTimer.singleShot(1500, self.take_screenshot)

#?Taking screenshots 
    def take_screenshot(self):
        screenshot_folder = "User_Inputs"
        screen = QApplication.primaryScreen()
        screenshot = screen.grabWindow(0)

        file_name = "screenshot_.png"
        file_path = os.path.join(screenshot_folder, file_name)
        screenshot.save(file_path, 'png')
        print(f"Screenshot saved to {file_path}")

        self.show() #Show the window again
        #!Functions to be executed after screenshot
        self.run_script()

#?Linked script to run GPT for SSS
    def run_script(self):
        self.open_window_2()    #Opening window 3 as soon as data recieved
        script_path = os.path.join(os.path.dirname(__file__), 'main_1_docs.py')
        subprocess.run(['python', script_path])

# #?Function to load output after data recieved from GPT
#     def load_text_from_file(self):
#         Text_Folder = "./"
#         file_path = os.path.join(Text_Folder, "output.txt")

#         if os.path.exists(file_path):
#             with open(file_path, "r") as file:
#                 content = file.read()
#                 self.textbox_2.setText(content)
#         else:
#             self.textbox_2.setText("No input file found.")



#!Function to restore the main window
    def restore_main_window(self):
        self.minimized_widget.hide()
        self.show()

#!Function to exit the main window
    def exit_window(self):
        sys.exit(app.exec_())

#!Function for adding paint to the window
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(0, 0, 0, 120))  # Changing the color of bg window
        painter.drawRect(self.rect())

#!Function to open the window_1
    def open_window_1(self):
        self.window2 = OverlayWindow_1()  # Create an instance of Window1
        self.window2.show()
        self.hide()

#!Function to open the window_2
    def open_window_2(self):
        # self.load_text_from_file()
        self.window2 = OverlayWindow_2()  # Create an instance of Window1
        self.window2.show()
        self.hide()

#!-------------------------------------------------------------------------------- OVERLAY_WINDOW_1------------------------------------------------------------------------------!#
#!-------------------------------------------------------------------------------- OVERLAY_WINDOW_1-----------------------------------------------------------------------------!#
#!-------------------------------------------------------------------------------- OVERLAY_WINDOW_1-----------------------------------------------------------------------------!#

class OverlayWindow_1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Overlay')
        self.setGeometry(200, 100, 600, 250)#Dimensions of window
        # | Qt.FramelessWindowHint
        self.setWindowFlags(Qt.WindowStaysOnTopHint| Qt.FramelessWindowHint )
        # self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.WindowTransparentForInput)
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
                font-size: 16px;            /* Increase font size */
                margin: 4px 2px;            /* Some margin */
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: white;    /* White background on hover */
                color: black;               /* Black text on hover */
                border: 2px solid #4CAF50;  /* Green border on hover */
            }
        """)
#* Adding button1
        self.button1 = QPushButton('Window 0', self)
        self.button1.clicked.connect(self.open_window_0)
        self.button1.setGeometry(80, 170, 200, 60)
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
                font-size: 16px;            /* Increase font size */
                margin: 4px 2px;            /* Some margin */
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: white;    /* White background on hover */
                color: black;               /* Black text on hover */
                border: 2px solid #4CAF50;  /* Green border on hover */
            }
        """)

#* Adding button2 for screenshot
        # self.button2 = QPushButton('Take Screenshot', self)
        # self.button2.setGeometry(80, 100, 200, 60)
        # self.button2.move(300, 100)
        # self.button2.clicked.connect(self.schedule_screenshot)
        # self.button2.setStyleSheet("""
        #     QPushButton {
        #         background-color: #958938;  /* Red background */
        #         color: white;               /* White text */
        #         font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
        #         font-weight: 800;
        #         border: none;               /* No border */
        #         padding: 14px 26px;         /* Some padding */
        #         text-align: center;         /* Centered text */
        #         text-decoration: none;      /* No underline */
        #         font-size: 16px;            /* Increase font size */
        #         margin: 4px 2px;            /* Some margin */
        #         border-radius: 6px;
        #     }
        #     QPushButton:hover {
        #         background-color: white;    /* White background on hover */
        #         color: black;               /* Black text on hover */
        #         border: 2px solid #f44336;  /* Red border on hover */
        #     }
        # """)

#* Adding textBox_1
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
        self.button3.clicked.connect(self.SS_and_saveInput)
        self.button3.setStyleSheet("""
            QPushButton {
                background-color: #1ea2bd;  /* Red background */
                color: white;               /* White text */
                font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                font-weight: 800;
                border: none;               /* No border */
                text-align: center;         /* Centered text */
                text-decoration: none;      /* No underline */
                font-size: 16px;            /* Increase font size */
                margin: 4px 2px;            /* Some margin */
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: white;    /* White background on hover */
                color: black;               /* Black text on hover */
                border: 2px solid #f44336;  /* Red border on hover */
            }
        """)

#* Button to run Run_script_text 
        self.button3 = QPushButton('Talk to me', self)
        self.button3.setGeometry(300, 155, 100, 40)
        self.button3.clicked.connect(self.userInput_and_sss)
        self.button3.setStyleSheet("""
            QPushButton {
                background-color: #1ea2bd;  /* Red background */
                color: white;               /* White text */
                font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
                font-weight: 800;
                border: none;               /* No border */
                text-align: center;         /* Centered text */
                text-decoration: none;      /* No underline */
                font-size: 16px;            /* Increase font size */
                margin: 4px 2px;            /* Some margin */
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
                font-size: 16px;            /* Increase font size */
                margin: 4px 2px;            /* Some margin */
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: white;    /* White background on hover */
                color: black;               /* Black text on hover */
                border: 2px solid #f44336;  /* Red border on hover */
            }
        """)

#* Button-5 to run the script for the GPT (To be combined with run screenshots)
        # self.button5 = QPushButton('Run GPT', self)
        # self.button5.setGeometry(400, 155, 100, 40)
        # self.button5.clicked.connect(self.run_script)
        # self.button5.setStyleSheet("""
        #     QPushButton {
        #         background-color: #958938;  /* Red background */
        #         color: white;               /* White text */
        #         font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
        #         font-weight: 800;
        #         border: none;               /* No border */
        #         text-align: center;         /* Centered text */
        #         text-decoration: none;      /* No underline */
        #         font-size: 16px;            /* Increase font size */
        #         margin: 4px 2px;            /* Some margin */
        #         border-radius: 6px;
        #     }
        #     QPushButton:hover {
        #         background-color: white;    /* White background on hover */
        #         color: black;               /* Black text on hover */
        #         border: 2px solid #f44336;  /* Red border on hover */
        #     }
        # """)


#?Function to save input, take screenshot_and_userQuery
    def SS_and_saveInput(self):
        self.save_input()
        self.clear_input()
        self.schedule_screenshot()

    
#!Saving Textbox input
    def save_input(self):
        Text_Folder = "User_Inputs"
        file_path = os.path.join(Text_Folder, "user_Input.txt")

        user_input = self.textbox.text()
        print(f"User input: {user_input} saved")  # Printing input in the terminal

        with open(file_path, "w") as file:  # Saving the file
            file.write(user_input + "\n")

        self.textbox.clear()

#!Calling run_script and saving the textbox input function simultaneously with single button click
    # def saveText_and_runScript(self):
    #     # Not able to clear the textbar is one major problem
    #     self.save_input()
    #     self.run_script_text()
#!Function to shift back to window_1
    def open_window_0(self):
        self.window1 = OverlayWindow_0()  # Create an instance of Window2
        self.window1.show()
        self.hide()

#!Function for calling combined sss and user query input
    def userInput_and_sss(self):
        script_path = os.path.join(os.path.dirname(__file__), './main_1_combined_Text_SSS.py')
        subprocess.run(['python', script_path])

    
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

#!Linked script to run input from text 
    def run_script_text(self):
        script_path = os.path.join(os.path.dirname(__file__), './main_3_textOutput.py')
        subprocess.run(['python', script_path])

#!Fxn to open Window-2
    def open_window_2(self):
        self.window2 = OverlayWindow_2()  # Create an instance of Window2
        self.window2.show()
        self.hide()


#!--------------------------------------------------------------------------------------OVERLAY_WINDOW-2-------------------------------------------------------------------------!#
#!--------------------------------------------------------------------------------------OVERLAY_WINDOW-2-------------------------------------------------------------------------!#
#!--------------------------------------------------------------------------------------OVERLAY_WINDOW-2-------------------------------------------------------------------------!#

class OverlayWindow_2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_text_from_file()  # Load text when initializing of sss
        # self.load_text_from_file_2()

    def initUI(self):
        self.setWindowTitle('Overlay')
        self.setGeometry(200, 100, 600, 600)
        # |Qt.FramelessWindowHint
        self.setWindowFlags(Qt.WindowStaysOnTopHint| Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:rgba(0, 0, 0, 0.7);")
        self.setWindowTitle("Window 2")

#!Adding a button to go back to previous window

#*Adding button1
        self.button1 = QPushButton('Window 1 clr', self)
        self.button1.clicked.connect(self.open_window_1 )
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
        self.button2 = QPushButton('Window 1', self)
        self.button2.clicked.connect(self.open_window_1)
        self.button2.setGeometry(400, 120, 200, 60)
        self.button2.setStyleSheet("""
            QPushButton {
                background-color: #795dec;  /* Green background */
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

#*Adding button3
        self.button3 = QPushButton('Window 1', self)
        self.button3.clicked.connect(self.open_window_1)
        self.button3.setGeometry(400, 200, 200, 60)
        self.button3.setStyleSheet("""
            QPushButton {
                background-color: #795dec;  /* Green background */
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

#*Adding button4
        self.button4 = QPushButton('Window 1', self)
        self.button4.clicked.connect(self.open_window_1)
        self.button4.setGeometry(400, 280, 200, 60)
        self.button4.setStyleSheet("""
            QPushButton {
                background-color: #795dec;  /* Green background */
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

#*Adding button5 for exiting the window
        self.button5 = QPushButton('Quit', self)
        self.button5.clicked.connect(self.exit_window)
        self.button5.setGeometry(400, 360, 200, 60)
        self.button5.setStyleSheet("""
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


#*Adding textbox_2 to display text (read only)
        vbox = QVBoxLayout()
        self.textbox_2 = QTextEdit(self)
        # self.textbox = QLineEdit(self)
        self.textbox_2.setReadOnly(True)
        self.textbox_2.setText('Initial Text')
        vbox.addWidget(self.textbox_2)
        self.setLayout(vbox)
        self.textbox_2.setGeometry(30, 15, 360, 360)
        self.textbox_2.setStyleSheet("""
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

#!Function to quit the window
    def exit_window(self):
        sys.exit(app.exec_())

#!Function to load output in the Window-2 textbox
    def load_text_from_file(self):
        Text_Folder = "./"
        file_path = os.path.join(Text_Folder, "output.txt")

        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                content = file.read()
                self.textbox_2.setText(content)
        else:
            self.textbox_2.setText("No input file found.")

#!Function to load output in the Window-2 textbox
    def load_text_from_file_2(self):
        Text_Folder = "./"
        file_path = os.path.join(Text_Folder, "output_Assistant.txt")

        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                content = file.read()
                self.textbox_2.setText(content)
        else:
            self.textbox_2.setText("No input file found.")


#!Function for the addition of the suggestion box
    def on_suggestion_selected(self, item):
        suggestion = item.text()
        # Generate output based on the suggestion
        output = f"Output for {suggestion}"
        self.output_textbox.setText(output)
    
#!Colors of the window
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(0, 0, 0, 120))  # Changing the color of bg window
        painter.drawRect(self.rect())

        self.show()
 
#!Function to shift back to window_1
    def open_window_1(self):
        self.window1 = OverlayWindow_1()  # Create an instance of Window2
        self.window1.show()
        self.hide()

#!Function to clear the saved info from textbox
    def clear_input(self):
        self.textbox_2.clear()

#!Showing the final window
if __name__ == '__main__':
    app = QApplication(sys.argv)
    overlay = OverlayWindow_0()
    overlay.show()
    sys.exit(app.exec_())