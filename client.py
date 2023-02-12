# Stephane Goulet

import socket
import threading
import sys

#Wait for incoming data from server
def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(1024)
            message = str(data.decode("utf-8"))
            print(message.strip("\n"))
            if ("Connection: Close" in message):
                print("Exiting...")
                quit()
        except:
            print("You have been disconnected from the server")
            signal = False
            break

#Get host and port
HOST = sys.argv[1]
PORT = int(sys.argv[2])

#Attempt connection to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
except:
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)

#Create new thread to wait for data
receiveThread = threading.Thread(target = receive, args = (sock, True))
receiveThread.start()

#Send data to server
while True:
    try:
        message = input()
    except ValueError:
        quit()
    message += "\n"
    sock.sendall(str.encode(message))