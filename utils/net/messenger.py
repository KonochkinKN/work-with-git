import socket
from _thread import *


USERS = {
    "192.168.88.129": "admin",
    "192.168.88.66": "Sergo",
    "192.168.88.76": "karyseel",
    "192.168.88.123": "Irz",
    "192.168.88.28": "Andrey",
    "192.168.88.135": "CIDER",
    "192.168.88.72": "OhMyGodAble"
}

PORTS = {
    "192.168.88.129": 12340,
    "192.168.88.66": 12341,
    "192.168.88.76": 12342,
    "192.168.88.123": 12343,
    "192.168.88.28": 12344,
    "192.168.88.135": 12345,
    "192.168.88.72": 12346
}

global HISTORY
HISTORY = {
    "192.168.88.129": "",
    "192.168.88.66": "",
    "192.168.88.76": "",
    "192.168.88.123": "",
    "192.168.88.28": "",
    "192.168.88.135": "",
    "192.168.88.72": ""
}


def receive_msg(con, sender):
    data = con.recv(1024)
    message = data.decode()
    HISTORY[sender] += f"\n{USERS[sender]}: {message}"
    con.close()


def send_msg(receiver, msg):
    client = socket.socket()
    port = PORTS[receiver]
    print((receiver, port))
    client.connect((receiver, port))
    client.send(msg.encode())
    host = socket.gethostbyname(socket.gethostname())
    HISTORY[receiver] += f"\n{USERS[host]}: {msg}"
    client.close()


def server_routine():
    server = socket.socket()
    host = socket.gethostbyname(socket.gethostname())
    port = PORTS[host]
    server.bind((host, port))
    server.listen(10)
    while True:
        con, sender = server.accept()
        start_new_thread(receive_msg, (con, sender[0]))


def dialog_menu(user):
    while True:
        print(HISTORY[user])
        print("Choose action:")
        print("1) Send message\t2) Quit\t*) Refresh dialog")
        action = input()
        if action == "1":
            message = input("Enter the message: ")
            send_msg(user, message)
        elif action == "2":
            break


def chat_menu():
    while True:
        print("Choose chat:")
        for i, u in enumerate(USERS.values()):
            print(f'{i+1}) {u}')
        print('0) Quit')
        user = int(input())
        if user == 0:
            break
        user = list(USERS.keys())[user-1]
        dialog_menu(user)


def init():
    start_new_thread(server_routine, ())
    chat_menu()


if __name__ == "__main__":
    init()
