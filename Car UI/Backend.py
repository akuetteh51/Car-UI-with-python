# project: Car UI with python
# Author: Michael Nana Kwame Akuetteh
#  date : 13/11/2020

import bluetooth
import CarBot
from tkinter import *


def Blue():
    print("hello")
    CarBot.info.insert(END,"Searching for devices...")
    CarBot.info.insert(END," ")
    nearby_devices = bluetooth.discover_devices()
    num = 0
    CarBot.info.insert(END, "Select your device by entering its coresponding number...")
    for i in nearby_devices:
        num += 1

        CarBot.info.insert(END,num + ": "+ bluetooth.lookup_name(i))
    selection = CarBot.info.get(ANCHOR)- 1
    # selection = CarBot.info.curselection(">") - 1

    sel=CarBot.tkinter.messagebox.askyesno("CarBot", "Confirm if you Have  the right bluetooth Option")
    if sel > 0:
        CarBot.info.insert(End,"Selection Selected")
    CarBot.info.insert(END,"You have selected" + bluetooth.lookup_name(nearby_devices[selection]))
    bd_addr = nearby_devices[selection]
    port= 1
sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
def Forward():
    print("Forward")
    data = "1"
    sock.send(data)

def Right():
    print("right")
    data = "2"
    sock.send(data)

def left():
    print("left")
    data = "3"
    sock.send(data)
def Backward():
    print("Backward")
    data = "4"
    sock.send(data)

def Stop():
    print("stop")
    data = "5"
    sock.send(data)

def speak():
    print("Say Something")
    data = "H"
    sock.send(data)