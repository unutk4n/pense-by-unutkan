## UNUTK4N ##
from tkinter import *
from tkinter import ttk
import time


text_1 = "Welcome to my first GUI app. "
space = "              "

deneme  = " "
def clock():
    
    current_time = time.localtime()
    show_time  = time.strftime("%H:%M", current_time)
    #time.sleep(5) # Just to go easy on the app. Don't need to go every second
    print(show_time)
    deneme = show_time
def headerdef():
    pass

def headerdef():
    pass

def headerdef():
    pass

def headerdef():
    pass


root = Tk()
root.title("UNUTK4N")


firstframe = ttk.Frame(root, width=700,height=500)# padding koymadım.
firstframe.grid(column=0,row=0, sticky=(N,W,E,S))

clock()

#it_related_left = ttk.Label(firstframe,text= space)
#it_related_left.grid(column=0,row=0)

it_related = ttk.Label(firstframe, text= text_1, )
it_related.grid(column=1, row=0, padx=10,pady=10)

time_widget = ttk.Label(firstframe, text=deneme)
time_widget.grid(column=2,row=0)



### HEADER OPTIONS
#



#



#



#



#






# column configure eklemedim.







root.mainloop()