import socket
import logging

class Beacon:

    def __init__(self, name, server_host, server_port):

        self.name = name
        self.server_host = server_host
        self.server_port = server_port
        self.ip = socket.gethostbyname(socket.gethostname())
        self.hostname = socket.gethostname()
        self.beacon_port = 0
        

    def send_msg(self, msg):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.connect((self.server_host, self.server_port))
            self.beacon_port = str(s.getsockname()[1])
            s.sendall(bytes(msg, 'utf-8'))
            data = s.recv(1024)
            data_string = data.decode("utf-8")
            logging.debug('Echo:' + str(data_string))

