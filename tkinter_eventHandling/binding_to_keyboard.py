from cgitb import text
from tkinter import * 
from tkinter import ttk

root = Tk()

#This will monitor all "Keypress events."
def key_press(event):
    print('type {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('character: {}'.format(event.char))
    print('keysym: {}'.format(event.keysym))
    print('keycode: {}'.format(event.keycode))

#Here i am binding an event to the enter button.
def key_press_enter(event):

    #I replace log.txt every time I press enter.
    if event.widget == entry:
        with open('log.txt',"w") as f:
            f.write(entry_text.get())


#This is a "Keypress fucntion"
root.bind('<KeyPress>',key_press)
root.bind('<Return>',key_press_enter)

entry_text = StringVar()
entry = ttk.Entry(root,textvariable=entry_text)
entry.pack()

#I can also bind to specific points, doesn't have to be in the 
#Entry widget

#entry.bind('<KeyPress>',key_press)

root.mainloop()

#Lots of event types we can bind
#Button Press
#Button Release
#Enter
#Leave
#Motion
#KeyPress
#KeyRelease
#Focus in 
#Focus out