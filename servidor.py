import socket
import _thread
import traceback


serverPort = 12000
conexoes = []
users = {}



def threaded(socketConexao):
    while True:
        try:
            data = socketConexao.recv(3096)
            if not data:
                conexoes.remove(socketConexao)
                socketConexao.close()
                break

            if users[socketConexao] == "userNameGenerico":
                users[socketConexao] = data.decode('ascii')
                mensagemInicial = "Usuarios conectados:"
                for conexao in conexoes:
                    usuario = users[conexao]
                    mensagemEntrou = users[socketConexao] + ' entrou no chat'
                    if  conexao != socketConexao:
                        conexao.send(mensagemEntrou.encode('ascii'))
                    mensagemInicial = mensagemInicial + " " + usuario + ", "
                mensagemInicial = mensagemInicial.encode('ascii')
                socketConexao.send(mensagemInicial)

            else:
                remetente = users[socketConexao]
                mensagem = remetente + ': ' + data.decode('utf-8')
                mensagemByte = mensagem.encode('utf-8')
                for conexao in conexoes:
                    if conexao != socketConexao:
                        conexao.send(mensagemByte)
        
        except Exception:
            conexoes.remove(socketConexao)
            socketConexao.close()
            break


if __name__ == '__main__':
    try:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind(('',serverPort))
        serverSocket.listen()
        print('O chat está aberto')
        while True:
            socketConexao, addr = serverSocket.accept()
            conexoes.append(socketConexao)
            users[socketConexao] = "userNameGenerico"
            _thread.start_new_thread(threaded, (socketConexao,))


    except Exception:
        print(traceback.format_exc())
