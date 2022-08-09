from tkinter import * 
from tkinter import ttk
import os
from PIL import Image

def setImageAsGif(imagePath):
    
    if ".gif" in imagePath:
        return imagePath

    if ".png" in imagePath:
        img = Image.open(imagePath)
        newImagePath = imagePath.replace(".png",".gif")
        img.save(newImagePath)
        return newImagePath

#Relative path joining. This function 
relpath = lambda p: os.path.normpath(os.path.join(os.path.dirname(__file__), p))

root = Tk()
label = ttk.Label(root,text="Hello Simple GUI",wraplength=300,justify=CENTER,foreground='black',font=('Courier',12))
label.pack()
label.config(text='Hi there this is my test application')

label.img = PhotoImage(file=setImageAsGif(relpath('../images/anko_logo.png')))
label_logo = ttk.Label(root,image=label.img,text="Welcome to Anko",compound='top')
label_logo.pack()

root.mainloop()