import socket
import threading
import time


def client_send(client_obj, txt):
    client_obj.send(txt.encode())


def client_receive(client_obj, buff=1024):
    return client_obj.recv(buff).decode()


def client_thread_handle(client_obj):
    print("Server spawn new thread client...")
    client_send(client_obj, "Welcome\n" + "=" * 80 + "\n")
    client_send(client_obj, "Name : ")
    name = client_receive(client_obj)
    client_send(client_obj, "\nThank you {}\nGoodbye....".format(name, ))
    client_obj.close()


# create socket obj
sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# block server tcp
sock_obj.bind(('0.0.0.0', 9000))
sock_obj.listen(3)

while True:
    print("Waiting connection....")
    client_obj, client_addr = sock_obj.accept()
    print(client_obj, client_addr)

    threading.Thread(target=client_thread_handle, args=(client_obj,), daemon=True).start()

#     client_send(client_obj, "Welcome\n"+"="*80+"\n")
#     client_send(client_obj, "Name : ")
#     name = client_receive(client_obj)
#     client_send(client_obj, "\nThank you {}\nGoodbye....".format(name,))
#     client_obj.close()

#     while True:
#         print("Waiting data from client...")
#         rx_data = client_obj.recv(1024)
#         print(rx_data.decode('cp1252'))
#         tx_num = client_obj.send('data received'.encode())
#         print(tx_num)


