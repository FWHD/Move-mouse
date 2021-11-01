## finished?
##mke into trnsferrble ppliction
##interface

import pyautogui
import time
import random

import tkinter as tk
from tkinter import messagebox as mb

window = tk.Tk()

greeting = tk.Label(text="What are the settings?")
greeting.pack()


##settings

##insert settings for how long to lst plus how often to move

label = tk.Label(text="how many times to move?")
label.pack()
count2 = tk.Entry()
count2.pack()




label = tk.Label(text="how many seconds apart?")
label.pack()
seconds2 = tk.Entry()
seconds2.pack()


##count=int(input("how many times to move? "))
##seconds=int(input("how many seconds apart? "))


##TO DO lnguge functions for correct grmmr (e.g. moving one more time)

##button to get code started




def handle_click(event):
    seconds=int(seconds2.get())
    times=0
    count=int(count2.get())
    moved=0
    while count>0:
        x=random.randrange(50,500,step=2)
        y=random.randrange(50,500,step=2)
        print("moving to " + str(x) + " and " + str(y) )
        pyautogui.moveTo(x,y,2)
        count=count-1
        times=times+1
        print("moved " + str(times) + " times")
        time.sleep(seconds)
        print("moving " + str(count) + " more times");
    print("done")
    mb.showinfo(message="Done")

button = tk.Button(text="Let's move the mouse", width=25,height=5,bg="grey",fg="black")

button.bind("<Button-1>", handle_click)
button.pack()

window.mainloop()



##done


    





