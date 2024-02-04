# Run this file to test the text completion API to ensure our API key is working
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # This loads the environment variables from the .env file
client = OpenAI() # This will automatically use the OPENAI_API_KEY from the environment so make sure to set it up in the .env file
 
# Basic completion example
# completion = client.chat.completions.create(
#   model="gpt-4", # gpt-3.5-turbo can also be used
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Hello!"}
#   ]
# )

# print(completion.choices[0].message.content)



# Streaming example with chunk counter to visualize
stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Write an essay on the importance of the internet in the 21st century."}],
    stream=True,
)
chunkNumber = 1
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(f"Chunk {chunkNumber}: {chunk.choices[0].delta.content}")
        chunkNumber += 1