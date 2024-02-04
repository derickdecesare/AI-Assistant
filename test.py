# Run this file to test the text completion API to ensure our API key is working
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # This loads the environment variables from the .env file
client = OpenAI() # This will automatically use the OPENAI_API_KEY from the environment so make sure to set it up in the .env file
 

completion = client.chat.completions.create(
  model="gpt-4", # gpt-3.5-turbo can also be used
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message.content)