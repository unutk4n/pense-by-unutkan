from tkinter import *
from tkinter import ttk

root = Tk()
root.title("UNUTK4N")

first_frame = ttk.Frame(root, width=700, height=400)
first_frame.grid(column=0, row=0, sticky=(N, W, E, S))
first_frame.grid_propagate(False)

buttons = []
for i in range(1, 4):
    for j in range(1, 4):
        button = ttk.Button(first_frame, text="Click me!")
        button.grid(row=i, column=j, sticky=(N, W, E, S), padx=5, pady=5)
        buttons.append(button)

root.mainloop() 