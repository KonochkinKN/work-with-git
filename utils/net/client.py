import socket
 
client = socket.socket()            # создаем сокет клиента
# hostname = socket.gethostname()     # получаем хост локальной машины
hostname = "192.168.88.66"
port = 12341                        # устанавливаем порт сервера
client.connect((hostname, port))    # подключаемся к серверу
message = socket.gethostbyname(socket.gethostname()) + "NICKNAME"   # вводим сообщение
client.send(message.encode())       # отправляем сообщение серверу
data = client.recv(1024)            # получаем данные с сервера
print("Server sent: ", data.decode()) 
client.close()                      # закрываем подключение
