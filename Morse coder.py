# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 18:08:11 2020

@author: henna
"""
#A morse code translator that translates input text into morse code

from tkinter import *
root = Tk()
root.title("Morse code translator")

e = Entry(root, width=100) #The box where you enter text you want to translate
e.grid(row=0,column=1)

space = Label(root, text="                    ") #Just to have some extra space between input and output lines
space.grid(row=1, column=1)

input_label=Label(root, text="Input:")
input_label.grid(row=0, column=0)

output_label = Label(root, text="Output:")
output_label.grid(row=2, column=0)

alphabet_morse = {
    "a": " .- ",
    "b": " -... ",
    "c": " -.-. ",
    "d": " -.. ",
    "e": " . ",
    "f": " ..-. ",
    "g": " --. ",
    "h": " .... ",
    "i": " .. ",
    "j": " .--- ",
    "k": " -.- ",
    "l": " .-.. ",
    "m": " -- ",
    "n": " -. ",
    "o": " --- ",
    "p": " .--. ",
    "q": " --.- ",
    "r": " .-. ",
    "s": " ... ",
    "t": " - ",
    "u": " ..- ",
    "v": " ...- ",
    "w": " .-- ",
    "x": " -..- ",
    "y": " -.-- ",
    "z": " --.. ",
    "0": " ----- ",
    "1": " .---- ",
    "2": " ..--- ",
    "3": " ...-- ",
    "4": " ....- ",
    "5": " ..... ",
    "6": " -.... ",
    "7": " --... ",
    "8": " ---.. ",
    "9": " ----. ",
    " ": " / "
    }


change_label = StringVar() #this variable is what changes the morse code translation as the play button gets pushed
change_label.set("")

def play_button():
    text_to_translate = str(e.get()) #get the text from the entry box e
    text_to_translate = text_to_translate.lower() #change text to lowercase so the letters will fit the values in the dictionary
    morse = ""

    for i in text_to_translate:
           if i in alphabet_morse:
               morse += alphabet_morse[i]
               
    change_label.set(morse) #set the change_label to morse to display the translated text          
    output_text = Label(root, textvariable=change_label) 
    output_text.grid(row=2, column=1)
    e.delete(0, END) #empty the entry box
    

play_button = Button(root, text="Play", command=play_button)
play_button.grid(row=0, column=2)


root.mainloop()
