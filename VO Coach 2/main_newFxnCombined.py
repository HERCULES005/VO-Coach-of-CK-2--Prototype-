import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLineEdit, QLabel, QFileDialog)
import base64
import requests  # Assuming requests is already installed
import json
import time
import pyautogui  # For capturing screenshots
import openai

# OpenAI API Key

class ScreenshotApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.screenshot_button = QPushButton("Capture Screenshot")
        self.screenshot_button.clicked.connect(self.take_screenshot)

        self.user_query_label = QLabel("Enter your query about the screenshot:")
        self.user_query_input = QLineEdit()

        self.solution_label = QLabel("Solution:")
        self.solution_output = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(self.screenshot_button)
        layout.addWidget(self.user_query_label)
        layout.addWidget(self.user_query_input)
        layout.addWidget(self.solution_label)
        layout.addWidget(self.solution_output)

        self.setLayout(layout)

        self.setWindowTitle("Screenshot Assistant")
        self.show()
    openai.api_key = "sk-proj-SCZ8qegWu2hEGGWlgbyJT3BlbkFJj7Pqi8BYVJUBO4qVX1Aq"  # Replace with your key


    def process_and_respond(image_path, user_query):
        start = time.time()

        # Encode the image if provided
        base64_image = None
        image_path = "User_Inputs\screenshot_.png"
        if image_path:
            print("Encoding image...")
            with open(image_path, "rb") as image_file:
                base64_image = base64.b64encode(image_file.read()).decode('utf-8')

        # Prepare the message payload for OpenAI
        messages = []
        if base64_image:
            messages.append({
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What’s in this image? , Provide the description in bullet points."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            })
        messages.append({
            "role": "user",
            "content": user_query
        })

        payload = {
            "model": "gpt-4o",
            "messages": messages,
            "max_tokens": 300
        }

        # Send the request to OpenAI
        print("Sending request to OpenAI...")
        response = requests.post("https://api.openai.com/v1/chat/completions", headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai.api_key}"
        }, json=payload)

        # Process the response
        output = response.json()
        content = output.get("choices", [])[0].get("message", {}).get("content", "")

        end = time.time()
        print(f"Time taken: {end - start:.2f} seconds")

        return content


    def take_screenshot(self):
        # Capture screenshot using pyautogui
        screenshot = pyautogui.screenshot()

        # Save screenshot dialog
        filename, _ = QFileDialog.getSaveFileName(self, "Save Screenshot", "", "PNG Images (*.png)")
        
