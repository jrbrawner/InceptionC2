from random import random
import socket
import base64
import re
import threading
import json
import logging
from .Beacon import Beacon


class ServerMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(ServerMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Server(metaclass=ServerMeta):
    # Set up methods with try/catch 

    def __init__(self, name):
        self.name = name
        self.ip = socket.gethostbyname(socket.gethostname())
        self.hostname = socket.gethostname()
        self.port = 12345
        self.addr = (self.ip, self.port)
        self.connection_list = {}

    def start_server(self):
        """Initialize the server to listen for incoming connections."""
        
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
                
    
    def create_beacon(self, name):
        """Create new beacon."""

        if name == '':
            name = 'Beacon' + str(len(self.connection_list))

        beacon = Beacon(name, self.ip, self.port)
        self.connection_list[beacon.name] = beacon

        return beacon

    def send_message_to_beacon(self, beacon_name, beacon_message):

        beacon = self.connection_list[beacon_name]
        print(beacon.name)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.connect((beacon.ip, beacon.beacon_port))
            s.sendall(bytes(beacon_message, 'utf-8'))


    def check_beacon_list(self):
        """Display list of created beacons."""
        for i in self.connection_list:
            print (i.name)

    

