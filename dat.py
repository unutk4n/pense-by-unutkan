from tkinter import *
from tkinter import ttk
import functions

# LET'S TRY TO MAKE IT MORE READABLE!
root = Tk()
root.title("UNUTK4N")





first_frame = ttk.Frame(root,width=700, height=400)
first_frame.grid(column=0,row=0, sticky=(N,W,E,S))
first_frame.grid_propagate(False)

# NUMBER 1 
widget1_1 = ttk.Button(
    first_frame,
    text= "Buy",
    command= functions.fundamental_press # without parenthesis.
)
widget1_1.grid(
    row=1,
    column=1,
    sticky=(N,W,E,S)
)

# NUMBER 2
widget1_2 = ttk.Button(
    first_frame,
    text= "Calculator ",
    command= functions.calculator
        
)
widget1_2.grid(
    row=1,
    column=2,
    sticky=(N,W,E,S)
)
# NUMBER 3
widget1_3 = ttk.Button(
    first_frame,
    text= "Click me!",
        
)
widget1_3.grid(
    row=1,
    column=3,
    sticky=(N,W,E,S)
)
# NUMBER 4
widget2_1 = ttk.Button(
    first_frame,
    text= "Click me!",
        
)
widget2_1.grid(
    row=2,
    column=1,
    sticky=(N,W,E,S)
)
# NUMBER 5
widget2_2 = ttk.Button(
    first_frame,
    text= "Click me!",
        
)
widget2_2.grid(
    row=2,
    column=2,
    sticky=(N,W,E,S)
)
# NUMBER 6
widget2_3 = ttk.Button(
    first_frame,
    text= "Click me!",
        
)
widget2_3.grid(
    row=2,
    column=3,
    sticky=(N,W,E,S)
)
# NUMBER 7
widget3_1 = ttk.Button(
    first_frame,
    text= "Click me!",
        
)
widget3_1.grid(
    row=3,
    column=1,
    sticky=(N,W,E,S)
)
# NUMBER 8
widget3_2 = ttk.Button(
    first_frame,
    text= "Click me!",
        
)
widget3_2.grid(
    row=3,
    column=2,
    sticky=(N,W,E,S)
)

# NUMBER 9
widget3_3 = ttk.Button(
    first_frame,
    text= "Click me!",
        
)
widget3_3.grid(
    row=3,
    column=3,
    sticky=(N,W,E,S)
)

widget4_1 = ttk.Label(
    first_frame,
    text=functions.widget4_1_text    
)
widget4_1.grid(
    row=2,
    column=4,
    sticky=(N,W,E,S)
)

root.mainloop( )  