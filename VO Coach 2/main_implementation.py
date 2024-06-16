import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                             QLabel, QLineEdit)
from PIL import ImageGrab
import requests


# Get your OpenAI API key from https://beta.openai.com/account/api-keys
OPENAI_API_KEY = "sk-proj-SCZ8qegWu2hEGGWlgbyJT3BlbkFJj7Pqi8BYVJUBO4qVX1Aq"


def check_api_version():
    """Checks OpenAI API version and provides guidance."""
    try:
        # Replace with the actual endpoint for checking API version (if available)
        response = requests.get("https://api.openai.com/version")
        response.raise_for_status()  # Raise an exception for non-200 status codes
        print("OpenAI API version seems valid. Proceeding...")
    except requests.exceptions.RequestException as e:
        print(f"Error checking API version: {e}")
        print("**Warning:** The provided code might need adjustments based on the latest API.")


def capture_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")  # Optional: Save screenshot
    print("Screenshot captured!")


def send_query(query):
    url = "https://api.openai.com/v1/completions"  # Update with the correct endpoint
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "text-davinci-003",  # Replace with appropriate model
        "prompt": f"Given the screenshot and the following query: {query}\nWhat is the solution?",
        "max_tokens": 1024,
        "n": 1,
        "stop": None,
        "temperature": 0.7,
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        answer = response.json()["choices"][0]["text"].strip()
        print(f"OpenAI Response: {answer}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending query to OpenAI: {e}")
        print("**Please check your API key and internet connection.**")


class ScreenshotQueryApp(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Check API version for informative guidance (optional)
        check_api_version()

        screenshot_button = QPushButton("Capture Screenshot")
        screenshot_button.clicked.connect(capture_screenshot)
        layout.addWidget(screenshot_button)

        self.screenshot_label = QLabel("")
        layout.addWidget(self.screenshot_label)

        self.query_input = QLineEdit()
        layout.addWidget(self.query_input)

        send_query_button = QPushButton("Send Query to OpenAI")
        send_query_button.clicked.connect(lambda: send_query(self.query_input.text()))
        layout.addWidget(send_query_button)

        self.answer_label = QLabel("")
        layout.addWidget(self.answer_label)

        self.setLayout(layout)

        self.setWindowTitle("Screenshot Query App")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScreenshotQueryApp()
    sys.exit(app.exec_())
