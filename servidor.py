import socket
import _thread
import traceback


serverPort = 12000
jogadores = []



class Jogador:
    def __init__(self):
        self.vida = 20
        self.ataque = 0
        self.defesa  = 0

    def setVida(self, vida):
        self.vida = vida

    def getVida(self):
        return self.vida


    def setAtaque(self, ataque):
        self.ataque = ataque

    def getAtaque(self):
        return self.ataque

    
    def setDefesa(self, defesa):
        self.defesa = defesa

    def getDefesa(self):
        return self.defesa


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
            if(len(jogadores) == 0):
                print("Esperando 2 jogadores")
            if(len(jogadores) == 0):
                print("Esperando 2 jogadores")
            socketConexao, addr = serverSocket.accept()
            _thread.start_new_thread(threaded, (socketConexao,))

    except Exception:
        print(traceback.format_exc())