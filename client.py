import socket
import sys

## Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

## Get data from the command line and check if valid.
args = sys.argv
if(len(args) == 3 and args[2].isnumeric() and (int)(args[2]) in range(0, 65535)):
    port = (int)(args[2])
    ip = args[1]

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
else:
    s.close()