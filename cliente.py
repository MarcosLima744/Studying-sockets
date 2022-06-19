import socket 
import traceback
import _thread

serverName = 'localhost'
serverPort = 12000

try:
    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
except Exception:
    print(traceback.format_exc())


def sendMessage(Socket):
    while True:
        data = input()
        data = data.encode('utf-8')
        try:
            Socket.send(data)
        except Exception:
            print(traceback.format_exc())


def recMessage(Socket):
    while True:
        try:
            mensagem = Socket.recv(3096)
            mensagem = mensagem.decode('utf-8')
            print(mensagem)

        except Exception:
            print(traceback.format_exc())



_thread.start_new_thread(sendMessage, (clientSocket,))
_thread.start_new_thread(recMessage, (clientSocket,))

while True:
    pass
