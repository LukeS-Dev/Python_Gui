from tcpFunctions import *
from tkinter import messagebox
import json

class TCP():
    def __init__(self):
        self.tcp = ''

    def setIP(self,strIp,strPort,status):
        ip = strIp.get()
        port = int(strPort.get())

        self.ip = ip
        self.port = port
        
        print(ip + " : " + str(port))

        self.tcp = TCPHandler(ip,port,timeout=2)
        
        response = self.tcp.connect()
        
        if response == "invalid":
            messagebox.showerror(title="Invalid IP", message="IP or port failed the check")
        elif response == "connect failed":
            messagebox.showerror(title="Connection unsuccessful", message="Connection to the given IP has failed.")
        elif response == "success":
            #messagebox.showinfo(title="Connection Established", message="Connection Established with " + ip + ":" + str(port))
            TCP.deleteAndInsert(status,"Connection Established with " + ip + ":" + str(port))
            with open('tcpConfig.txt',"w") as f:
                config = {
                    "ip" : ip,
                    "port" : port
                }
                f.write(json.dumps(config))

    def sendText(self,text,status): 
        message = text.get('1.0','end-1c')
        try: 
            response = self.tcp.sendStr(message)
            if response == "success":
                TCP.deleteAndInsert(status,"Sent :\n" + message + "\n\nTo : \n" + self.ip + ":" + str(self.port))
                #messagebox.showinfo(title="Sent", message="Sent :\n" + message + "\n\nTo : \n" + self.ip + ":" + str(self.port))
            elif response == "fail":
                messagebox.showerror(title="Send fail", message="Message failed to send")
        except: 
                messagebox.showerror(title="No Connection", message="No Connection Established")

    def deleteAndInsert(text,message):
        text.config(state = "normal")
        text.delete('1.0','end')
        text.insert('end',message)
        text.config(state = "disable")
