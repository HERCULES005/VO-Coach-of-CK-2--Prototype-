import openai

#Exporting the answer to the user query

openai.api_key = "sk-proj-SCZ8qegWu2hEGGWlgbyJT3BlbkFJj7Pqi8BYVJUBO4qVX1Aq"

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

file_path = 'User_Inputs/user_Input.txt'
file_content = read_file(file_path)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": file_content}
]

response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=messages
)

# Print the assistant's response
print(response.choices[0].message['content'])

# saving the output in a .txt file
with open("output_Assistant.txt", "w") as outfile:
  outfile.write(response.choices[0].message['content'])

