from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtCore import QDateTime
from PIL import Image
import pytesseract
import openai

# Capture the screenshot using PyQt5
app = QApplication([])
screen = QGuiApplication.primaryScreen()
screenshot = screen.grabWindow(0)
filename = QDateTime.currentDateTime().toString('yyyyMMddhhmmss') + '.png'
screenshot.save(filename, 'png')

# Load the screenshot image
screenshot_image = Image.open(filename)

# Perform OCR on the image
text = pytesseract.image_to_string(screenshot_image)

# Print the extracted text
print("Extracted Text:\n", text)

# Use OpenAI API to analyze the text with a custom prompt
openai.api_key = 'your-api-key-here'

custom_prompt = """
The following text is extracted from a screenshot. Please provide a detailed analysis, including any relevant context, potential issues, and actionable insights:

Extracted Text:
"""

complete_prompt = custom_prompt + text

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=complete_prompt,
    max_tokens=500
)

print("Analysis:\n", response.choices[0].text.strip())
