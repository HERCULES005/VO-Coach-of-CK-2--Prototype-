import openai
import json

# file paths
file_path1 = './User_Inputs/user_Input.txt'
file_path2 = 'output.txt'
output_file_path = 'embeddings_output_2.txt'

openai.api_key = 'sk-proj-sCeQ2SU6fWh2wTluOETfT3BlbkFJIqGF8dcW1gFkKI12r1Bj'

with open(file_path1, 'r', encoding='latin-1') as f: #Utf-8 encoding wont work somehow so latin-1 encoding is dont to read the input
    text1 = f.read()

with open(file_path2, 'r', encoding='latin-1') as f:
    text2 = f.read()

# Concatenate sss and User query
combined_text = text1 + "\n" + text2


# Create embeddings
response = openai.Embedding.create(
    input=combined_text,
    model="text-embedding-ada-002"
)

embeddings = response['data'][0]['embedding']
print(embeddings)


with open(output_file_path, 'w', encoding='latin-1') as f:
    f.write(json.dumps(embeddings))

print(f"Embeddings have been saved to {output_file_path}")