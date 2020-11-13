# project: Car UI with python
# Author: Michael Nana Kwame Akuetteh
#  date : 13/11/2020

from tkinter import *
import Backend
import tkinter.messagebox
# Initializing Window

win=Tk()
win.iconbitmap(r'icon.ico')
win.title("CarBot")
win.resizable(0,0)
# icons for buttons
forw=PhotoImage(file="forward.png")
backw=PhotoImage(file="backward.png")
lef=PhotoImage(file="left .png")
rig=PhotoImage(file="right.png")
stop=PhotoImage(file="stop.png")
blu=PhotoImage(file="Bluetooth.png")
speak=PhotoImage(file="speaker.png")

# widgets
blue=Button(win,image=blu,command=Backend.Blue)
blue.grid(row=0,column=0,bd=None)
# info box
info =Listbox(win,height=12,width=80)
info.grid(row=0,column=5)

# Controls Buttons
forwd=Button(win,image=forw, command=Backend.Forward)
forwd.grid(row=1,column=2)

backwd=Button(win,image=backw,command=Backend.Backward)
backwd.grid(row=3,column=2)

lefwd=Button(win,image=lef,command=Backend.left)
lefwd.grid(row=2,column=0)
St=Button(win,height=4,width=12)
St.grid(row=2,column=1,columnspan=2)
rigwd=Button(win,image=rig,command=Backend.Right)
rigwd.grid(row=2,column=3)

Stop=Button(win,image=stop,command=Backend.Stop)
Stop.grid(row=2,column=6)
Sp=Button(win,image=speak,command=Backend.speak)
Sp.grid(row=3,column=5)

win.mainloop()

