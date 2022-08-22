import socket
import base64
import re
import threading
import json
import logging

class Server:
    # Set up methods with try/catch
    def __init__(self, name):
        self.name = name
        self.ip = socket.gethostbyname(socket.gethostname())
        self.hostname = socket.gethostname()
        self.port = 12345
        self.addr = (self.ip, self.port)
        self.connection_list = []


    def start_server(self):
        
        listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen.bind(self.addr)
        listen.listen(1)
        
        while True:
            logging.debug('Waiting for connection')
            
            connection, address = listen.accept()
            with connection:
                logging.debug('Connection received from:' + str(address))
                data = connection.recv(1024)
                if not data: 
                    logging.error('Error, non bytes data received.')
                connection.sendall(data)

                if bytes('kill', 'utf-8') in data:
                    logging.debug('Kill command sent.')
                    print('Kill command sent.')
                    break
                
