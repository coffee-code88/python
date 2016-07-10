import  socket
import signal
import sys
import threading

class Server:
    def __init__(self, config):
        signal.signal(signal.SIGINIT, self.shutdown)
        self.serverSocket = socket.socket(socket.AF_INT, socket.SOCK_STREAM)
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serverSocket.bind((config['HOST_NAME'], config['BIND_PORT']))
        self.serverSocket.listen(10)
        self.__clients = {}

    def listenForClients():
        while True:
            (clientSocket, client_address) = self.serverSocket.accept()
            d = threading.Thread(name=self.__getClientName(client_address), target = self.proxy_thread, args=(clientSocket, client_address))
            d.setDaemon(True)
            d.start()
            
                 

