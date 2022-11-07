import socket
import sys

def addToGroup(address, name):
  
  if name not in dictMembers:
    ## Add the member to the group
    myName = data.decode("utf-8").split()[1]
    dictMembers[myName] = address
    dictMessage[myName] = []

    ## Send to the client all the members in the group
    firstName = (str)(list(dictMembers.keys())[0])

    if (firstName != myName):
        groupNames = firstName 
        for i in range(1, len(dictMembers)):
          key = (str)(list(dictMembers.keys())[i])
          if (key != myName):
            groupNames += ", " + (str)(key)
            
        s.sendto(str.encode(groupNames), address)
    else:
        s.sendto(b'', address)


    ## Send a message to all the members that that someone has joined
    for i in range(0, len(dictMembers)):
        key = (str)(list(dictMembers.keys())[i])
        if (key != myName):
          joinMessage = myName + ' has joined'
          (dictMessage[key]).append(str.encode(joinMessage))      


args = sys.argv
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if (len(args) == 1):
  port = 12345
else:
  port = (int)(args[1])

s.bind(('', port))
dictMembers = {}
dictMessage = {}

while True:
    data, addr = s.recvfrom(1024)
    if ((str)(data) != "b''"):
      dataStr = data.decode("utf-8")
      num = dataStr.split()[0]
      if (num == '1'):
        addToGroup(addr, dataStr)
    
    print(dictMembers)


  