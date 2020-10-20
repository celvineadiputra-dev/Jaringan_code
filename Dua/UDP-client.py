import socket
import time

ip_udp_server = "127.0.0.1"
udp_port_server = 10000

sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# for i in range(5):
#     sock_udp.sendto("#{} Ini Pesan UDP\n".format(i).encode(),(ip_udp_server,udp_port_server))
#     time.sleep(0.1)

i = 0
sock_udp.sendto("#{} Ini Pesan UDP\n".format(i).encode(),(ip_udp_server,udp_port_server))

# udp_rx = sock_udp.recvfrom(32)
# print(udp_rx)

print("UDP FINISH !!!")
