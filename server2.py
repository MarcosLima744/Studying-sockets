import socket
import _thread
import traceback


serverPort = 12000

def threaded(socketConexao):
    data = socketConexao.recv(1024)
    data = data.decode()
    data = data[::-1]
    print(data)
    data = data.encode('ascii')
    socketConexao.send(data)
    socketConexao.close()


if __name__ == '__main__':
    try:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind(('',serverPort))
        serverSocket.listen(1)
        print('Já pode mandar')
        while True:
            socketConexao, addr = serverSocket.accept()
            _thread.start_new_thread(threaded, (socketConexao,))

    except Exception:
        print(traceback.format_exc())