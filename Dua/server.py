import socket


def client_send(client_obj, txt):
    client_obj.send(txt.encode())


def client_receive(client_obj, buff=1024):
    return client_obj.recv(buff).decode()


# create socket obj
sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# block server tcp
sock_obj.bind(('127.0.0.1', 5000))
sock_obj.listen(3)

while True:
    print("Waiting connection...")
    client_obj, client_addr = sock_obj.accept()
    print(client_obj, client_addr)

    client_send(client_obj, "Welcome\n" + "=" * 80 + "\n")
    client_send(client_obj, "Name : ")
    name = client_receive(client_obj)
    client_send(client_obj, "\nThank You {}\nGoodbye...".format(name, ))
    client_obj.close()