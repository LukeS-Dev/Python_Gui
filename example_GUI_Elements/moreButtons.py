from tkinter import *
from tkinter import ttk


def whatSpam(message,label):
    label.config(text=message)

def whatBreakie(breakfast):
    print(breakfast)

window = Tk()
window.geometry("300x300")

spam = StringVar()
checkbutton = ttk.Checkbutton(  window, 
                                text = "Spam?",
                                variable = spam, 
                                onvalue ='SPAM!!!!', 
                                offvalue = 'NO SPAMMM',
                                command = lambda: whatSpam(spam.get(),label))

checkbutton.pack()

label = ttk.Label(window,text="NO SPAMMM")
label.pack()


breakfast = StringVar()
breakfast.set("No breakkie :( ")

ttk.Radiobutton(window,text="SPAM",variable=breakfast,value='SPAM').pack()
ttk.Radiobutton(window,text="food",variable=breakfast,value='food').pack()
ttk.Radiobutton(window,text="otherFood",variable=breakfast,value='otherFood').pack()

button = ttk.Button(window,
                    text = "Check Breakfast",
                    command = lambda: whatBreakie(breakfast.get()))

button.pack()
checkbutton.config(textvariable=breakfast)

window.mainloop()