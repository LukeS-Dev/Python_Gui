from tkinter import *
from tkinter import ttk

root = Tk()

notebook = ttk.Notebook(root)
notebook.pack()

frame1 = ttk.Frame(notebook,padding=20,relief=SUNKEN)
ttk.Button(frame1,text = 'Click Me!').pack()

frame2 = ttk.Frame(notebook,padding=20,relief=SUNKEN)

notebook.add(frame1,text='One')
notebook.add(frame2,text = 'two')

#adding and forgetting new frame.
frame3 = ttk.Frame(notebook,padding=20,relief=SUNKEN)
notebook.insert(1,frame3,text="three")
notebook.forget(1)

#TAB METHOD configure
#notebook.tab(1, state='disabled')
#This functions returns values/Properties of first tab.
#notebook.tab(1) 

root.mainloop()