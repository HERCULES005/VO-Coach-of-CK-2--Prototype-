import openai
import base64
import time
import requests
import json

# OpenAI API Key
openai.api_key = "sk-proj-SCZ8qegWu2hEGGWlgbyJT3BlbkFJj7Pqi8BYVJUBO4qVX1Aq"

start = time.time()

# Function to read text input from path
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

file_path = 'User_Inputs/user_Input.txt'
file_content = read_file(file_path)

# Path to your image
image_path = "User_Inputs/screenshot_.png"

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {openai.api_key}"
}

# Create the content describing the image
# image_description = f"The image provided is encoded as follows: {base64_image[:100]}... (truncated for brevity)"

# Create the messages payload
messages = [
    {"role": "system", "content": "Answer to user's query in as short as possible,answer to user's query should be related to screenshot only nothing else no any other references(if possible) , you are a helpful assistant"},
    {"role": "user", "content": file_content},
    {"role": "user", "content": [
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]}
]

# Make the API call to OpenAI's ChatCompletion
response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=messages,
    max_tokens=300
)
# Response 2 for user's provided image
response_2 = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=messages)
output = response_2.json()


content = response.choices[0]['message']['content']
# content_2 = output.get("choices", [])[0].get("message", {}).get("content", "")
content_2 = output


# print(f"content_1 = {content} and \n \n \n content_2 = {content_2}")
print(f"content_1 = {content}")

# with open("output.txt", "w") as outfile:
#     outfile.write(content)

end = time.time()

print("Response saved to output.txt")
print(f"Time taken: {end - start} seconds")
