from tkinter import *
from tkinter import ttk

#Root is root element of the window. 
root = Tk()

#ttk - maintains styles between operating systems. 
#intialize button with text - Click me
#pack function to display it.
button = ttk.Button(root,text='Click Me')
button.pack()

#Indexing method shown below to "extract" text 
getElement = button['text']
button['text'] = 'Press Me'
button.config(text= 'Push Me')

#Doing this will return dictonary with full 
#configuration field
getConfig = button.config()

#This method gets the unique button identifier that 
#is generated by Tkinter.
widgetNameIdentifier = str(button)
print(widgetNameIdentifier)

#You can directly pack a button configuration into 
#the root/page, but then this can't be referenced later. E.G
ttk.Label(root,text= " Hello World").pack()