#Imports the functions to record the audio
import pyaudio
import wave
import time
import sounddevice as sd


#This variable creates a custom name for the file that is the current time of completed script
timestr = time.strftime("%Y%m%d-%H%M%S")
#This sets up the recording and defines objects

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
#RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME =timestr+'.wav'
MINS=int(input("How Many Minutes would you like to record?"))
#RECORD_SECONDS=(MINS*60)
#print(MINS)
SECS =int(60)
RECORD_SECONDS=MINS*SECS
#print(SECS)
print(RECORD_SECONDS)




audio = pyaudio.PyAudio()

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print ("recording...")


frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)


# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
