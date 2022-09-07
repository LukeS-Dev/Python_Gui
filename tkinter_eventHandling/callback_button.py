from tkinter import * 
from tkinter import ttk

root = Tk()

#Default callback. 
def callback():
    print('Call back!')

ttk.Button(root,text="Click",command=callback).pack()

def callback_num(input):
    print(f"Number {input}")

#In this we use lambda to pass the value. 
#Lambda functions don't execute on startup.
ttk.Button(root,text="Click 1",command=lambda:callback_num(1)).pack()
ttk.Button(root,text="Click 2",command=lambda:callback_num(2)).pack()
ttk.Button(root,text="Click 3",command=lambda:callback_num(3)).pack()

root.mainloop()

#Widgets that have callbacks include. 

#Button
#Chcekbutton
#RadioButton
#Spinbox
#Scale
#Scrollbar