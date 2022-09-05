import socket

#Format HEX string to a byte array. This is required for E355.
def StringToHex(strIn):
    numBytes = 2
    hexOut = bytearray()
    for index in range(0,len(strIn),numBytes):
        hexOut.append(int(strIn[index:index+numBytes],16))
    return hexOut

#Check if IP string is valid.
def checkIPString(ip): 
    parts = ip.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if not isinstance(int(part), int):
            return False
        if int(part) < 0 or int(part) > 255:
            return False

    return True 

def convertIPHexToStr(hexString):

    ipAddress = ''

    for i in range(0,len(hexString)-1,1):
        if i%2 == 0: 
            hex = int("0x" + hexString[i] + hexString[i+1],base=16)
            ipAddress = ipAddress + str(hex) + '.' if i != len(hexString) - 2 else ipAddress + str(hex)

    return ipAddress

def checkIPHexString(hexString):
    isHexValid = True
    errorMsg = "No Error"
    hexDigits = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","a","b","c","d","e","f"]

    if len(hexString) != 8:
        isHexValid = False
        #errorMsg = "Invalid IP Length"
    else: 
        for i in hexString: 
            if i not in hexDigits:
                isHexValid = False 

                #errorMsg = "Invalid Hexidecimal String"

    return isHexValid   

#Class to handle TCP connection with E355
class TCPHandler: 
    def __init__(self,ip,port,timeout=60):
        self.ip = TCPHandler.checkIP(ip)
        self.port = port
        self.timeout = timeout
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Socket on IPV4 TCP/IP

    def connect(self):
        if self.ip != "invalid":
            try: 
                self.socket.connect((self.ip,self.port))
                return "success"
            except:
                return "connect failed"
        else: 
            return "invalid"

    def disconnect(self): 
        self.socket.close()

    def sendStr(self,message):
        try: 
            self.socket.send(message.encode())
            return "success"
        except:
            return "fail"

    def send(self,message):
        self.socket.send(StringToHex(message))

    def read(self):
        self.socket.settimeout(self.timeout)
        try:
            reply = self.socket.recv(1024).hex().upper()
        except:
            reply = ""
        self.socket.settimeout(None)
        return reply

    def checkIP(ip):
        #print(checkIPString(ip),checkIPHexString(ip))
        if checkIPString(ip) == True:
            return ip
        elif checkIPHexString(ip) == True:
            return convertIPHexToStr(ip)
        else:
            return "invalid"
        