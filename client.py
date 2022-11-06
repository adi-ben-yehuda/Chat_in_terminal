import socket
import sys

args = sys.argv
ip = args[1]
port = (int)(args[2])
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
count = 3 ## Amount of messages

while True:
    if (len(args) > count):
        command = args[count] + ' ' + args[count + 1]
        commandBytes = str.encode(command)
        
        count = count + 2
        s.sendto(commandBytes, (ip, port))
        data, addr = s.recvfrom(1024)
        print(str(data), addr)


##s.close()