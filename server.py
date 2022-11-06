import socket
import sys

def addToGroup(address, name):
  ##justname = name.split('b')[1]
  if name not in dict:
    dict[address] = (str)(name).split()[1].split("'")[0]



args = sys.argv

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = (int)(args[1])
s.bind(('', port))
dict = {}


while True:
    data, addr = s.recvfrom(1024)
    num = (str)(data.split()[0]).split("'")[1]
    if (num == '1'):
      addToGroup(addr, str(data))

    
    print(str(data), addr)
    print(num)
    print(dict)
    s.sendto(data.upper(), addr)


  