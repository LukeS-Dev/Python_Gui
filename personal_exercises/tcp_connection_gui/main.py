from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from guiFunctions import * 
import json

root = Tk()
root.geometry("400x300")
root.title("TCP Data Senders")

tcpObject = TCP()

ipConfig = Frame(root).pack()

def printIpInfo():
    print(ipAddress.get())
    print(portEntry.get())

#Ip address entry point
ttk.Label(ipConfig,text="Enter an IP").pack()

ipAddress = StringVar()
ipEntry = ttk.Entry(ipConfig,textvariable=ipAddress)
ipEntry.pack()

ttk.Label(ipConfig,text="Enter a Port number").pack()
port = StringVar()
portEntry = ttk.Entry(ipConfig,textvariable=port)
portEntry.pack()

try: 
    with open("tcpConfig.txt","r") as f:
        config = json.loads(f.read())
        keys = config.keys()
        if "ip" in keys:
            ipEntry.insert(0,config["ip"])
        if "port" in keys:
            portEntry.insert(0,config["port"])
        print(config)
except: 
    with open("tcpConfig.txt","w") as f: 
        f.write(json.dumps({"ip" : "" , "port" : ""}))


ttk.Button(ipConfig, text = "Show IP", command=printIpInfo).pack()
ttk.Button(ipConfig, text = "Connect", command = lambda : tcpObject.setIP(ipAddress,port)).pack()

tcpSend = Frame(root).pack()
ttk.Label(text = "Send message ").pack(pady=10)
text = Text(tcpSend,width = 50, height = 5, wrap = 'word',state='normal')
text.pack()

ttk.Button(tcpSend,text = "Send",command = lambda:tcpObject.sendText(text)).pack()


root.mainloop()