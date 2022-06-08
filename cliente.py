import socket
import threading 
import traceback



serverName = 'localhost'
serverPort = 12000


try:
    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    data = input()
    data = data.encode('ascii')
    clientSocket.send(data)
    setence = clientSocket.recv(1024)
    setence.decode()
    print(setence)
    clientSocket.close()

except Exception:
    print(traceback.format_exc())
