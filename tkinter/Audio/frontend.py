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
    WAVE_OUTPUT_FILENAME =timestr+'.wav'
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

#def view_command():
#    list1.delete(0,END)
#    for row in backend.view():
#        list1.insert(END,row)

#def add_command():
#    backend.add_shipment(tkvar.get(),firstname_title.get(),surname_title.get(),addr1_title.get(),addr2_title.get(),town_title.get(),pcode_title.get(),service.get(),con_title.get(),quantity_title.get(),prod.get())
#    list1.delete(0,END)
#    list1.insert(END,(tkvar.get(),firstname_title.get(),surname_title.get(),addr1_title.get(),addr2_title.get(),town_title.get(),pcode_title.get(),service.get(),con_title.get(),quantity_title.get(),prod.get()))

#def search_command():
    #list1.delete(0,END)
    #for row in backend.search(tkvar.get(),firstname_title.get(),surname_title.get(),addr1_title.get(),addr2_title.get(),town_title.get(),pcode_title.get(),service.get(),con_title.get(),quantity_title.get(),prod.get()):
    #    list1.insert(END,row)

#def export_command():
    #backend.export()


window=Tk()

window.wm_title("Audio")


l1=Label(window,text="How Many Minutes do you want to record?")
l1.grid(row=0,column=2)
MIN=IntVar()
e1=Entry(window,textvariable=MIN)
e1.grid(row=0,column=3)



#list1=Listbox(window, height=12,width=40)
#list1.grid(row=6,column=3,rowspan=12,columnspan=2)

#sb1=Scrollbar(window)
#sb1.grid(row=7,column=5,rowspan=6)

#list1.configure(yscrollcommand=sb1.set)
#list1.configure(yscrollcommand=sb1.set)
#sb1.configure(command=list1.yview)

#b1=Button(window,text="View All", width=12)
#b1.grid(row=7,column=5)

b2=Button(window,text="Record", width=10,command=audio)
b2.grid(row=0, column=5)


window.mainloop()
