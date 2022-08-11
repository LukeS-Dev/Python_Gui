from tkinter import *
from tkinter import ttk
import random

def printEntryField(target,prefix = ""):
    print(prefix + target.get())

def insertRandomNameIntoEntryField(target,names):
    name = names[random.randint(0,len(names) - 1)]
    target.delete(0,3000)
    target.insert(0,name)

def printCredentials(user,password):
    printEntryField(user,"Username : ")
    printEntryField(password, "Password : ")


#generate list of names for random function
names = []
with open("names.txt","r") as file:
    for line in file:
        names.append(line.replace("\n",""))


#Initalize main window. 
window = Tk()

#Create frame for entering Name
frame_userEntry = ttk.Frame(window,padding=20)
frame_userEntry.pack()

# Create label and entry field of 30 
label = ttk.Label(frame_userEntry,text="Please enter a name").pack()
entry = ttk.Entry(frame_userEntry,width=30)
entry.pack()

#Create another frame for user input.
frame_buttons = ttk.Frame(window,padding = 10)
frame_buttons.pack()

button_getName = ttk.Button(frame_buttons,
                            text="getName",
                            width = 20,
                            command= lambda: printEntryField(entry))
button_getName.pack()

button_setRandomName = ttk.Button(frame_buttons,
                            text="Random name",
                            width = 20,
                            command= lambda: insertRandomNameIntoEntryField(entry,names))

button_setRandomName.pack()

#Create a user name password entry method. Only frame init and fetch.
frame_credentials = frame_userEntry = ttk.Frame(window,padding=20)
frame_credentials.pack()

ttk.Label(frame_credentials,text="Enter username").pack()

entry_userName = ttk.Entry(frame_credentials,
                            width=20)
                            
entry_userName.pack()

ttk.Label(frame_credentials,text="Enter Password").pack()

entry_password = ttk.Entry(frame_credentials,
                            width=20,
                            show = "*")
entry_password.pack()

button_getCredentials = ttk.Button(frame_credentials,
                            text="Get Credentials",
                            width = 20,
                            command= lambda: printCredentials(entry_userName,entry_password))

button_getCredentials .pack()

window.mainloop()