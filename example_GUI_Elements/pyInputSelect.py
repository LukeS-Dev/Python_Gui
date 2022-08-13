from tkinter import *
from tkinter import ttk

#Generic Window
window = Tk()
window.geometry("300x300")

#Month Select
month = StringVar()
monthSelect = ttk.Combobox(window,
                            textvariable = month,
                            values=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])

monthSelect.pack()

#Year select
year = StringVar()
Spinbox(window,from_ = 1900, to = 2100, textvariable = year).pack()
year.set(2000)

window.mainloop()