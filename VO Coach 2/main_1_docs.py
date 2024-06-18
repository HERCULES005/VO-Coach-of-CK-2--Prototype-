import base64
import requests
import os
import json
import time

# OpenAI API Key
api_key = "sk-proj-SCZ8qegWu2hEGGWlgbyJT3BlbkFJj7Pqi8BYVJUBO4qVX1Aq"

start = time.time()
# Function to encode the image
def encode_image(image_path):
  print("GPT is processing data")
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "User_Inputs/screenshot_.png"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4o",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What’s in this image? , Provide the description in bullet points"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}


response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
output = response.json()
end = time.time()
# print(output)
# Save the json data in a text file
content = output.get("choices", [])[0].get("message", {}).get("content", "")

# with open("output.json", "w") as outfile:
#     json.dump(output, outfile, indent=4)
print(content)
with open("output.txt", "w") as outfile:
    outfile.write(content)

print("Response saved to output.json")
print (f"time taken : {end - start}")


