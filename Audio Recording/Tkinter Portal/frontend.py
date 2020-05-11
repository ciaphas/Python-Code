from tkinter import *
import sounddevice as sd
import wave
import time
from scipy.io.wavfile import write


def record():
	import backend
	record()
	


window=Tk()

fs = 44100


window.wm_title("Lecture Recorder")

rec_seconds=int(60)
seconds=int()


l1=Label(window, text="Lecture Title")
l1.grid(row=1, column =2)
lecture_name=StringVar()
e1=Entry(window,textvariable=lecture_name)
e1.grid(row=1, column=3)

l2=Label(window, text="How many minutes is the Lecture?")
l2.grid(row=2, column =2)
minutes=IntVar()
e2=Entry(window, textvariable=minutes)
e2.grid(row=2, column =3)


b1=Button(window,text="Record", width=12, command=record)
b1.grid(row=2, column = 5)





window.mainloop()
