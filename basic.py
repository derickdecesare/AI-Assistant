# These are basic examples of how to use the OpenAI API

# Imports
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()  # This loads the variables from .env into the environment

client = OpenAI() # This will automatically use the OPENAI_API_KEY from the environment so make sure to set it up in the .env file




############### STEP 1##########################################
# Speech to Text #
audio_file= open("/path/to/file/audio.mp3", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
# returns a json object:
# {
#   "text": "Imagine the wildest idea that you've ever had, and you're curious about how it might scale to something that's a 100, a 1,000 times bigger.
# ....
# }


############### STEP 2 ##########################################
# Text Generation By GTP4 #
completion = client.chat.completions.create(
  model="gpt-4", # gpt-3.5-turbo can also be used
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

# print(completion.choices[0].message.content) # This will print the response from the GPT-4 model


# EXAMPLE RESPONSE
# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "message": {
#         "content": "The 2020 World Series was played in Texas at Globe Life Field in Arlington.",
#         "role": "assistant"
#       },
#       "logprobs": null
#     }
#   ],
#   "created": 1677664795,
#   "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
#   "model": "gpt-3.5-turbo-0613",
#   "object": "chat.completion",
#   "usage": {
#     "completion_tokens": 17,
#     "prompt_tokens": 57,
#     "total_tokens": 74
#   }
# }


################ STREAMING Generation ###################
stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")





################ STEP 3 #########################################
# Text To Speach #
# Hit's API endpoint that will return a MP3 file of speech with the provided text
speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

response.stream_to_file(speech_file_path)

# REAL TIME STREAMING TO REDUCE LATENCY ----> THIS IS GOING TO BE THE MAIN FOCUS ---> Means we can play the audio file as it is being generated
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Hello world! This is a streaming test.",
)

response.stream_to_file("output.mp3")











