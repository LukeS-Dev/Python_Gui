import socket
import argparse
import json
import os
import time

parser = argparse.ArgumentParser()
parser.add_argument('-gc','--generateConfig', action = 'store_true',
                    help="Generates a default configuration")
args = parser.parse_args()

if args.generateConfig == True:
    with open("tcpConfig.txt","w") as f: 
        f.write(json.dumps({"ip": "127.0.0.1", "port": "8888"}))

#Call Main file as background task
os.system("START /B python main.py")
time.sleep(0.5)

#Open TCP server
host = "127.0.0.1"
port = 8888
address = (host,port)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
print("Starting Server...")
server.bind(address)
server.listen(1)
exit = False

while exit == False:
    connection, client_address = server.accept()

    try: 
        print("Connection from: ", client_address)

        while True: 
            data = connection.recv(1024)
            recv_length = len(data)
            print("recieved : ", data.decode("utf-8"))
            if recv_length == 0:
                break

    finally: 
        connection.close()
        exit = True