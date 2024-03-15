#UNUTK4N

import random
from tkinter import *
from tkinter import ttk
global widget4_1_text
widget4_1_text = " asşldkaşsldk"
print(widget4_1_text)
def fundamental_press():
    print("CONTROL UNIT FUNDAMENTAL PRESS")
    global widget4_1_text
    widget4_1_text = "SENIN PARAN MI VAR FAKIR ! ! "
    print(widget4_1_text)
    return widget4_1_text
    

#print (help(random))

def calculator():
    calc_root= Tk()
    calc_root.title("CALCULATOR")
    
    calc_frame = ttk.Frame(calc_root, width=400, height=700)
    calc_frame.grid(row=0,column=0, sticky=(N,W,E,S))
    
    calc_root.mainloop()
    




