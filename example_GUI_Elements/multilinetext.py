##aim -> Create a send and recieve (automatic) function.
#This function has get method.
from tkinter import *
from tkinter import ttk
root = Tk()

def printMessage(message,printTarget=0):
    if printTarget == 0:
        print(message.get())
    else: 
        printTarget.configure(state='normal')
        printTarget.insert('end + 1 line', "Sent : " + message.get())
        printTarget.insert('end + 2 line', "\nmessage recieved\n\n")
        printTarget.configure(state='disabled')

def printFullTextLog(target):
    print(target.get('1.0','end'))

frame = ttk.Frame(root,padding=10)
frame.pack()

#Initialize text box. 
ttk.Label(frame,text="traffic Log").pack()
text = Text(frame,width = 60, height = 30, wrap = 'word',state='disabled')
text.pack()

#send message with input
frame_input = ttk.Frame(root,padding=10)
frame_input.pack()

ttk.Label(frame_input,text="Message to Send").pack()
sendMsg = ttk.Entry(frame_input,width = 60)
sendMsg.pack()

#put message to box
sendButton = ttk.Button(frame_input,
                        text="Send",
                        command=lambda: printMessage(sendMsg,text))
sendButton.pack()

#Print full traffic.
ttk.Button(frame_input,
            text='Print Full message',
            command=lambda: printFullTextLog(text)).pack()

root.mainloop()