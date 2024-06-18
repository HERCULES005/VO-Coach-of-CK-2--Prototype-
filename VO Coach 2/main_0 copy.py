from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QTextEdit
import os
import sys
import openai
import base64

class OverlayWindow_1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Overlay')
        self.setGeometry(200, 100, 600, 400)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:rgba(0, 0, 0, 0.7);")

        # Adding button to open Window 2
        self.button1 = QPushButton('Window 2', self)
        self.button1.clicked.connect(self.open_window_2)
        self.button1.setGeometry(80, 300, 200, 60)
        self.button1.setStyleSheet(self.button_style("#4CAF50"))

        # Adding button to take screenshot
        self.button2 = QPushButton('Take Screenshot', self)
        self.button2.setGeometry(300, 300, 200, 60)
        self.button2.clicked.connect(self.schedule_screenshot)
        self.button2.setStyleSheet(self.button_style("#f44336"))

        # Adding textbox for user input
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Enter text here...")
        self.textbox.setGeometry(50, 30, 500, 50)
        self.textbox.setStyleSheet(self.textbox_style())

        # Adding button to save input
        self.button3 = QPushButton('Enter', self)
        self.button3.setGeometry(400, 90, 150, 40)
        self.button3.clicked.connect(self.save_input)
        self.button3.setStyleSheet(self.button_style("#f44336"))

        # Adding button to clear input
        self.button4 = QPushButton('Clear', self)
        self.button4.setGeometry(400, 140, 150, 40)
        self.button4.clicked.connect(self.clear_input)
        self.button4.setStyleSheet(self.button_style("#bdbdbd"))

        # Adding textbox for the question
        self.question_box = QLineEdit(self)
        self.question_box.setPlaceholderText("Ask a question about the screenshot...")
        self.question_box.setGeometry(50, 180, 500, 50)
        self.question_box.setStyleSheet(self.textbox_style())

        # Adding button to process screenshot and question
        self.button5 = QPushButton('Ask Question', self)
        self.button5.setGeometry(400, 240, 150, 40)
        self.button5.clicked.connect(self.process_screenshot_and_question)
        self.button5.setStyleSheet(self.button_style("#4CAF50"))

    def button_style(self, color):
        return f"""
            QPushButton {{
                background-color: {color};
                color: white;
                font-family: 'Lucida Sans', sans-serif;
                font-weight: 800;
                border: none;
                padding: 14px 26px;
                text-align: center;
                font-size: 16px;
                margin: 4px 2px;
                border-radius: 6px;
            }}
            QPushButton:hover {{
                background-color: white;
                color: black;
                border: 2px solid {color};
            }}
        """

    def textbox_style(self):
        return """
            QLineEdit {
                background-color: rgba(255, 255, 255, 0.7);
                font-family: 'Lucida Sans', sans-serif;
                font-weight: 600;
                color: black;
                padding: 10px;
                border: 2px solid #cccccc;
                border-radius: 10px;
                font-size: 16px;
            }
            QLineEdit:focus {
                border: 2px solid #4CAF50;
            }
        """

    def save_input(self):
        Text_Folder = "User_Inputs"
        os.makedirs(Text_Folder, exist_ok=True)  # Ensure the folder exists
        file_path = os.path.join(Text_Folder, "user_Input.txt")
        user_input = self.textbox.text()
        print(f"User input: {user_input} saved")
        with open(file_path, "w") as file:
            file.write(user_input + "\n")
        self.textbox.clear()

    def clear_input(self):
        self.textbox.clear()

    def schedule_screenshot(self):
        QTimer.singleShot(1000, self.prepare_screenshot)

    def prepare_screenshot(self):
        self.hide()
        QTimer.singleShot(1500, self.take_screenshot)

    def take_screenshot(self):
        screenshot_folder = "User_Inputs"
        os.makedirs(screenshot_folder, exist_ok=True)  # Ensure the folder exists
        screen = QApplication.primaryScreen()
        screenshot = screen.grabWindow(0)
        file_name = "screenshot_.png"
        file_path = os.path.join(screenshot_folder, file_name)
        screenshot.save(file_path, 'png')
        print(f"Screenshot saved to {file_path}")
        self.show()

    def process_screenshot_and_question(self):
        screenshot_folder = "User_Inputs"
        screenshot_path = os.path.join(screenshot_folder, "screenshot_.png")
        question = self.question_box.text()

        # Call a function to process the screenshot and question
        response = self.process_with_gpt(screenshot_path, question)
        print(f"Response: {response}")

        # Optionally, display the response in a new window or textbox

    def process_with_gpt(self, screenshot_path, question):
        # OpenAI GPT-4 integration to process the screenshot and question
        openai.api_key = "sk-proj-SCZ8qegWu2hEGGWlgbyJT3BlbkFJj7Pqi8BYVJUBO4qVX1Aq"

        with open(screenshot_path, "rb") as image_file:
            image_data = image_file.read()
        
        # Use a new model and proper API call for GPT-3.5-turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Read images and provide a description of the image along with query provided by the user"},
                {"role": "user", "content": f"Here is a screenshot of some code: {screenshot_path}\nQuestion: {question}\nAnswer:"}
            ]
        )
        return response.choices[0].message["content"].strip()

    def open_window_2(self):
        self.window2 = OverlayWindow_2()
        self.window2.show()
        self.hide()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(0, 0, 0, 120))
        painter.drawRect(self.rect())

class OverlayWindow_2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_text_from_file()

    def initUI(self):
        self.setWindowTitle('Overlay')
        self.setGeometry(200, 100, 600, 600)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:rgba(0, 0, 0, 0.7);")

        self.button1 = QPushButton('Window 1 clr', self)
        self.button1.clicked.connect(self.open_window_1)
        self.button1.setGeometry(400, 40, 200, 60)
        self.button1.setStyleSheet(self.button_style("#795dec"))

        self.button2 = QPushButton('Window 1', self)
        self.button2.clicked.connect(self.open_window_1)
        self.button2.setGeometry(400, 120, 200, 60)
        self.button2.setStyleSheet(self.button_style("#795dec"))

        self.button3 = QPushButton('Window 1', self)
        self.button3.clicked.connect(self.open_window_1)
        self.button3.setGeometry(400, 200, 200, 60)
        self.button3.setStyleSheet(self.button_style("#795dec"))

        self.button4 = QPushButton('Window 1', self)
        self.button4.clicked.connect(self.open_window_1)
        self.button4.setGeometry(400, 280, 200, 60)
        self.button4.setStyleSheet(self.button_style("#795dec"))

        self.textbox = QTextEdit(self)
        self.textbox.setReadOnly(True)
        self.textbox.setGeometry(40, 40, 340, 500)
        self.textbox.setStyleSheet(self.textbox_style())

    def button_style(self, color):
        return f"""
            QPushButton {{
                background-color: {color};
                color: white;
                font-family: 'Lucida Sans', sans-serif;
                font-weight: 800;
                border: none;
                padding: 14px 26px;
                text-align: center;
                font-size: 16px;
                margin: 4px 2px;
                border-radius: 6px;
            }}
            QPushButton:hover {{
                background-color: white;
                color: black;
                border: 2px solid {color};
            }}
        """

    def textbox_style(self):
        return """
            QTextEdit {
                background-color: rgba(255, 255, 255, 0.7);
                font-family: 'Lucida Sans', sans-serif;
                font-weight: 600;
                color: black;
                padding: 10px;
                border: 2px solid #cccccc;
                border-radius: 10px;
                font-size: 16px;
            }
            QTextEdit:focus {
                border: 2px solid #795dec;
            }
        """

    def load_text_from_file(self):
        Text_Folder = "User_Inputs"
        os.makedirs(Text_Folder, exist_ok=True)  # Ensure the folder exists
        file_path = os.path.join(Text_Folder, "user_Input.txt")
        with open(file_path, "r") as file:
            text = file.read()
            self.textbox.setText(text)

    def open_window_1(self):
        self.window1 = OverlayWindow_1()
        self.window1.show()
        self.hide()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(0, 0, 0, 120))
        painter.drawRect(self.rect())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window1 = OverlayWindow_1()
    window1.show()
    sys.exit(app.exec_())
