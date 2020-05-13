from tkinter import *
#import backend
#from shutil import copyfile
import pyaudio
import wave
import time


def audio():
    #This variable creates a custom name for the file that is the current time of completed script
    timestr = time.strftime("%Y%m%d-%H%M%S")
    #This sets up the recording and defines objects

    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    #RECORD_SECONDS = 10
    NAMES = NAME.get()
    WAVE_OUTPUT_FILENAME =NAMES+'.wav'
    MINS = MIN.get()
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



window=Tk()

window.wm_title("Audio Lecture Recorder")


l1=Label(window,text="How Many Minutes do you want to record?")
l1.grid(row=1,column=2)
MIN=IntVar()
e1=Entry(window,textvariable=MIN)
e1.grid(row=1,column=3)
l2=Label(window, text="Name of your Lecture")
l2.grid(row=0,column=2)
NAME=StringVar()
e2=Entry(window,textvariable=NAME)
e2.grid(row=0,column=3)


b2=Button(window,text="Record", width=10,command=audio)
b2.grid(row=1, column=5)
b3=Button(window,text="Exit", width=10, command=exit)
b3.grid(row=2, column=5)


window.mainloop()
