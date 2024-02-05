import pyaudio
import wave
import audioop
import math

# Constants
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
SILENCE_THRESHOLD = 20
SILENCE_DURATION = 2  # seconds of silence to stop recording

audio = pyaudio.PyAudio()

# Start recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

frames = []
silent_chunks = 0
is_silent = True

print("Recording...")

while True:
    data = stream.read(CHUNK)
    rms = audioop.rms(data, 2)  # Get RMS of data

    if rms > SILENCE_THRESHOLD:
        frames.append(data)
        silent_chunks = 0
        is_silent = False
    elif not is_silent:
        # If it's silent, increment the silent chunk count
        silent_chunks += 1
        frames.append(data)

        # If we've had enough silent chunks, break the loop
        if silent_chunks > SILENCE_DURATION * (RATE / CHUNK):
            break

print("Finished recording.")

# Stop and close the stream 
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded data as a WAV file
with wave.open("output.wav", "wb") as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

# Convert WAV to MP3
import subprocess
subprocess.call(['ffmpeg', '-i', 'output.wav', 'output.mp3'])
