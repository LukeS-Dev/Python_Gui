from tkinter import *
from tkinter import ttk

window = Tk()
frame = ttk.Frame(window,
                height=100,
                width=200,
                relief = RIDGE,
                padding = (40,20))

frame.pack()

ttk.Button(frame,text = 'Click').grid()

ttk.LabelFrame(window,heigh = 100, width = 200, text = 'My Config').pack()

window.mainloop()