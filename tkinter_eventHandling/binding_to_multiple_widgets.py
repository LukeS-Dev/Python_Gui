from tkinter import *
from tkinter import ttk

root = Tk()

label1 = ttk.Label(root,text='Label 1')
label2 = ttk.Label(root,text='Label 2')

label1.pack()
label2.pack()

#Tk will prioritise button because it is more specific. 
label1.bind('<ButtonPress>',lambda e: print("Lambda1 pressed"))
label1.bind('<1>',lambda e: print("button 1 pressed"))

#This will trigger two events. 
root.bind('<1>',lambda e: print("root button 1."))

#Unbing and give priority to main
label1.unbind('<1>')
label1.unbind('<ButtonPress>')

root.mainloop()