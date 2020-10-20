# pip install netaddr
# pip install netifaces
# Nama : Celvine Adi Putra | 1721250017
from netaddr import *
import ipaddress
import netifaces
import pprint


def Ipv4subnet(subnet):
    ipMaskBinary = ""
    ipMaskBinary = ipMaskBinary.join([bin(int(oct))[2:] for oct in subnet.split(".")])

    isBitZero = subnet[0] == "0"
    for bit in ipMaskBinary[1:]:
        if bit == "1" and isBitZero:
            return False

        if bit == "0":
            isBitZero = True

    return True


Ipaddress = input('Masukkan Ip address V4 :')
Ipaddress = IPAddress(Ipaddress)
subnet = input('Masukkan Subnet mask : ')

print("Yang anda masukkan Ip vesi : %d" % (Ipaddress.version))
subnetValid = Ipv4subnet(subnet)
if Ipaddress.version == 4 and subnetValid:
    print("Bit Biner Ipaddress : ", format(Ipaddress.bits()))
    ipandsubnet = str(Ipaddress) + "/" + subnet
    SB = ipaddress.IPv4Network(ipandsubnet,False)
    
    print("Subnet")
    print(SB[0])
    print("Broadcast")
    br = SB[-1]
    print(br)
    
    print("IP address yang bisa digunakan")
    for index, addr in enumerate(SB):
        if index != 0 and br != addr:
            print(addr)
            
    gateways = netifaces.gateways()
    default_gateway = gateways['default'][netifaces.AF_INET][0]
    print("Ip Gateway : " + (default_gateway))

elif Ipaddress.version != 4:
    print("Ip yang dimasukkan bukan Ipv4")
elif not subnetValid:
    print("Subnet Mask yang dimasukkan tidak valid")
