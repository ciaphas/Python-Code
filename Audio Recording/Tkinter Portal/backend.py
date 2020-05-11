import sounddevice as sd
import wave
import time
from scipy.io.wavfile import write
import frontend


def record():
	seconds=frontend.seconds
	lecture_name=frontend.lecture_name
	myrecording = sd.rec(int(seconds *fs), samplerate=fs, channels=2)
	sd.wait()
	write('lecture_name'+'.wav', fs, myrecording)

