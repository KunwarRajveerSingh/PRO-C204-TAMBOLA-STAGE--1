import socket
from tkinter import *
from threading import Thread
import random
from PIL import ImageTk, Image

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None

canvas1 = None

playerName = None
nameEntry = None
nameWindow = None


def askPlayerName():
    global playerName
    global nameEntry
    global namewindow
    global Canvas1

    namewindow = Tk()
    namewindow.title("Tanbola Family Fun")
    namewindow.geometry("800x600")

    screen_width = namewindow.winfo_screenwidth()
    screen_height = namewindow.winfo_screenheight()
    bg = ImageTk.PhotoImage(file = "./assets/background1.png")
    Canvas1 = Canvas(namewindow,width= 500,height = 580)

    Canvas1.pack(fill = "both", expand = True)
    Canvas1.create_image( 0, 0, image = bg, anchor="nw")
    Canvas1.create_text(screen_width/4.5, screen_height/5, text = "Enter Name", font=("Chalkboard SE",60), fill="black")
    nameEntry = Entry(namewindow, width=15, justify='center', font=('Chalkboard SE' , 38), bd=5, bg="white")
    nameEntry.place(x = screen_width/7, y=screen_height/4 )

    button = Button (namewindow, text="Save", font=("Chalkboard SE", 38), width=11, command="saveName", height=2, bg="#80deea", bd=3)
    button.place(x = screen_width/6, y=screen_height/3)
    namewindow. resizable(True, True)
    namewindow.mainloop()

def recivedMsg():
    pass

def saveName():
    global SERVER
    global playerName
    global namewindow
    global nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0, END)
    namewindow.destroy()

    SERVER.send(playerName.encode())

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT = 6000
    IP_ADDRESS = "127.0.0.1"

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    thread = Thread(target=recivedMsg)
    thread.start()

    askPlayerName()

setup()