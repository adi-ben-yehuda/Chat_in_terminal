import socket
import sys

args = sys.argv
ip = args[1]
port = (int)(args[2])
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'', (ip, port))

while True:
    args = sys.argv
    message = input()
    s.sendto(str.encode(message), (ip, port))
    data, addr = s.recvfrom(1024)
    print(data.decode("utf-8"))
##s.close()