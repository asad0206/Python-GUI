import pygame
from pygame import mixer
from tkinter import *
import os

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()
def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()
def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()
def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause()

root=Tk()
mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

playlist=Listbox(root,selectmode=SINGLE,bg="Black",fg="white",font=('system',10),width=50)
playlist.grid(columnspan=10)
os.chdir(r'C:\Users\Asad Ansari\Music')
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn=Button(root,text="Play",command=playsong,bg="Black",fg="Green")
playbtn.config(font=('times',15),bg="DodgerBlue2",fg="white",padx=7,pady=7)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('times',15),bg="DodgerBlue2",fg="white",padx=7,pady=7)
pausebtn.grid(row=1,column=1)

stopbtn=Button(root,text="Stop",command=stopsong)
stopbtn.config(font=('times',15),bg="DodgerBlue2",fg="white",padx=7,pady=7)
stopbtn.grid(row=1,column=2)

Resumebtn=Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('times',15),bg="DodgerBlue2",fg="white",padx=7,pady=7)
Resumebtn.grid(row=1,column=3)
mainloop()