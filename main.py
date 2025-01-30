import pyaudio
import wave
from shazamio import Shazam
import asyncio

format = pyaudio.paInt16
channels = 1
rate = 44100
chunk = 1024
record_sec = 10
output_file = 'output.wav'

p = pyaudio.PyAudio()

stream = p.open(channels=channels,rate=rate,input=True,format=format,frames_per_buffer=chunk)

print('Recording audio(10s)....')

frames=[]
for i in range(0,int(rate/chunk * record_sec)):
    data = stream.read(chunk)
    frames.append(data)
print('Record Completed....')
stream.stop_stream()
stream.close()
p.terminate()

with wave.open(output_file,'wb') as wf:
    wf.setnchannels(channels)
    wf.setframerate(rate)
    wf.setsampwidth(p.get_sample_size(format))
    wf.writeframes(b''.join(frames))

async def identify_song(audio_file):
    shazam = Shazam()
    out = await shazam.recognize(audio_file)
    print(out)

asyncio.run(identify_song(output_file))