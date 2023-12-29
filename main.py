# Importing necessary modules
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

# Initializing the Tkinter root window
root = Tk()
root.title("Text To Speech")
root.geometry("900x450")
root.resizable(False, False)
root.configure(bg="purple")

# Initializing the text-to-speech engine
engine = pyttsx3.init()

# Function to speak the entered text
def speakNow():
    # Getting the text from the text area
    text = text_area.get(1.0, END)
    # Getting selected gender and speed from the comboboxes
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    
    # Getting available voices
    voices = engine.getProperty('voices')
    
    # Function to set voice based on gender and speak the text
    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    # Checking if text is entered
    if (text):
        # Setting the speech rate based on selected speed
        if (speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()

# Function to download the spoken text as an MP3 file
def download():
    # Getting the text from the text area
    text = text_area.get(1.0, END)
    # Getting selected gender and speed from the comboboxes
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    
    # Getting available voices
    voices = engine.getProperty('voices')
    
    # Function to set voice based on gender and save the text as an MP3 file
    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            # Asking user to select a directory to save the file
            path = filedialog.askdirectory()
            os.chdir(path)
            # Saving the text as an MP3 file
            engine.save_to_file(text, 'speech.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            # Asking user to select a directory to save the file
            path = filedialog.askdirectory()
            os.chdir(path)
            # Saving the text as an MP3 file
            engine.save_to_file(text, 'speech.mp3')
            engine.runAndWait()

    # Checking if text is entered
    if (text):
        # Setting the speech rate based on selected speed
        if (speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()

# Setting up the icon
image_icon = PhotoImage(file="speak.png")
root.iconphoto(False, image_icon)

# Top Frame
Top_Frame = Frame(root, bg="#C919BE", width=900, height=100)
Top_Frame.place(x=0, y=0)

# Adding a logo to the top frame
Logo = PhotoImage(file="mainlogo.png")
Label(Top_Frame, image=Logo, bg="#C919BE").place(x=1, y=1)
Label(Top_Frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="#C919BE", fg="black").place(x=100, y=30)

# Text area for entering text
text_area = Text(root, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

# Labels and comboboxes for selecting voice and speed
Label(root, text="VOICE", font="arial 15 bold", bg="black", fg="#C919BE").place(x=580, y=160)
Label(root, text="SPEED", font="arial 15 bold", bg="black", fg="#C919BE").place(x=760, y=160)

gender_combobox = Combobox(root, values=['Male', 'Female'], font="arial 14", state='r', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='r', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

# Buttons for speaking and downloading
imageicon = PhotoImage(file="speak.png")
btn = Button(root, text="SPEAK", compound=LEFT, width=10, font="arial 14 bold", command=speakNow)
btn.place(x=550, y=280)

save = Button(root, text="DOWNLOAD", compound=LEFT, width=10, bg="#39c79e", font="arial 14 bold", command=download)
save.place(x=730, y=280)

# Running the Tkinter main loop
root.mainloop()
