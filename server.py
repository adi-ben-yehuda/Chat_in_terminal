import socket
import sys

def addToGroup(address, name):
  
  if name not in dict:
    ## Add the member to the group
    myName = data.decode("utf-8").split()[1]
    dict[address] = myName

    ## Send to the client all the members in the group
    firstName = (str)(list(dict.values())[0])

    if (firstName != myName):
        groupNames = firstName 
        for i in range(1, len(dict)):
          value = (str)(list(dict.values())[i])
          if (value != myName):
            groupNames += ", " + (str)(value)
            
        s.sendto(str.encode(groupNames), address)

    ## Send a message to all the members that that someone has joined
    for i in range(0, len(dict)):
        value = (str)(list(dict.values())[i])
        if (value != myName):
          joinMessage = myName + ' has joined'
          s.sendto(str.encode(joinMessage), list(dict.keys())[i])
      


args = sys.argv
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if (len(args) == 1):
  port = 12345
else:
  port = (int)(args[1])

s.bind(('', port))
dict = {}

while True:
    data, addr = s.recvfrom(1024)
    if ((str)(data) != "b''"):
      dataStr = data.decode("utf-8")
      num = dataStr.split()[0]
      if (num == '1'):
        addToGroup(addr, dataStr)
    
    print(dict)


  