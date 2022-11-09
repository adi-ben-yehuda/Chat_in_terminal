import socket
import sys

## Get data from the command line
args = sys.argv
if (len(args) < 3):
    ip = '127.0.0.1'
    port = 12345
else:
    ip = args[1]
    port = (int)(args[2])

## Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
##s.sendto(b'', (ip, port))

## Get data from the user and send it to the server
while True:
    args = sys.argv
    message = input()
    s.sendto(str.encode(message), (ip, port))
    data, addr = s.recvfrom(1024)
    dataStr = data.decode("utf-8")
    if (dataStr != ''):
        ## When the user wants to leave the group
        if (dataStr == 'close'):
            s.close()
            break
        ## When the user wants to get updates
        elif (dataStr.isnumeric()):
            for i in range(0, (int)(dataStr)):
                update, addr = s.recvfrom(1024)
                print(update.decode("utf-8"))

        else: print(dataStr)