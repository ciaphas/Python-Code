import sounddevice as sd
import wave
import time
from scipy.io.wavfile import write

fs = 44100 #Sample RATE
minutes=int(input("How Many Minutes would you like to record?"))
rec_seconds=int(60)
name=str(input("What Lecture is this?"))
seconds=minutes*rec_seconds

myrecording = sd.rec(int(seconds *fs), samplerate=fs, channels=2)
sd.wait()
write(name+'.wav', fs, myrecording)
