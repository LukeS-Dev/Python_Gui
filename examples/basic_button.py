from tkinter import *
from tkinter import ttk 
import os


def callback():
    print("Clicked!")

root = Tk()
root.geometry("500x600")

#Relative path joining. This function 
relpath = lambda path: os.path.normpath(os.path.join(os.path.dirname(__file__), path))
button = ttk.Button(root,text='Click Me',command=callback,padding=[5,5,5,5])
button.pack(padx=0,pady=10)

#sets state to enabled
button.state(['disabled'])
#set state to disabled
button.state(['!disabled'])

button.img = PhotoImage(file=relpath('../images/anko_logo.gif'))

#Subsample can lower resolution and scale the 
small_img=button.img.subsample(2,2)
button.config(image=small_img,compound="top")


root.mainloop()