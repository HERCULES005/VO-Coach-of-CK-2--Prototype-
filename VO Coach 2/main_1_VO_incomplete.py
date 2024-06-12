from openai import OpenAI
import base64
import requests

# OpenAI API Key
api_key = "sk-proj-SCZ8qegWu2hEGGWlgbyJT3BlbkFJj7Pqi8BYVJUBO4qVX1Aq"

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "User_Inputs\screenshot_.png"
prompt_message = f"""<objective> You are a gaming expert, analyze the screen and suggest the best possible(valid) next move (according to rules of that game) to the player(if any).</objective>
  <context> 
      <TASK1>          Url for the game is: {url}. You first identify game from url string analyze it very efficently without leaving any proper notations related to that game</TASK1>
      <TASK2>          Analyze the image provided and determine the game being played (e.g., chess, checkers, go).</TASK2>
      <important>      WRITE THE EXPLANATION IN SUPER SIMPLE LANGUAGE(can be easily understood by a 5 year old too) in NOT MORE THAN 2-3 LINES</important>
      <Situation1>     If the screen shows anything like "TASK FAILED ,YOU FAILED or anything related to failed" simply react with seems like you failed don't worry just try again</Situation1>
      <Others>         NEVER *GO TO THE URL. NEVER RESPOND IN MORE THAN 3 LINES. If you see any vulgar content, just say - you are dirty and I am not talking to you. And if you see religious content, just say - I am not religious.</Others>
  </context> """

PROMPT_MESSAGES = {
        "role": "user",
        "content": [
            prompt_message,
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image}"}}
        ],
    }

# Parameters for API call
params = {
        "model": "gpt-4o",
        "messages": [PROMPT_MESSAGES],
        "max_tokens": 500,
    }

# Make the API call
result = client.chat.completions.create(**params)
# return result.choices[0].message.content
