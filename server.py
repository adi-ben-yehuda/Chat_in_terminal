import socket
import sys

 ## Add member to the group
def addToGroup(address, name):
  
  if name not in dictMembers:
    ## Add the member to the group
    dictMembers[name] = address
    dictMessage[name] = []

    ## Send to the client all the members in the group
    firstName = (str)(list(dictMembers.keys())[0])

    if (firstName != name):
        groupNames = firstName 
        for i in range(1, len(dictMembers)):
          key = (str)(list(dictMembers.keys())[i])
          if (key != name):
            groupNames += ", " + (str)(key)
            
        s.sendto(str.encode(groupNames), address)
    else:
        s.sendto(b'', address)


    ## Send a message to all the members that that someone has joined
    for i in range(0, len(dictMembers)):
        key = (str)(list(dictMembers.keys())[i])
        if (key != name):
          joinMessage = name + ' has joined'
          (dictMessage[key]).append(str.encode(joinMessage))      


## Send a message to all the members
def sendMessage(addr, data):
  dataMessage = data
  nameOfSend = list(dictMembers.keys())[list(dictMembers.values()).index(addr)]
  for i in range(0, len(dictMembers)):
      key = (str)(list(dictMembers.keys())[i])
      if (key != (str)(nameOfSend)):
        sendMessage = (str)(nameOfSend) + ': ' + dataMessage
        (dictMessage[key]).append(str.encode(sendMessage))



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
      num,dataMessage = dataStr.split(' ', 1)
      if (num == '1'):
        addToGroup(addr, dataMessage)
      if (num == '2'):
        sendMessage(addr,dataMessage)
    
    print(dictMembers)
    print(dictMessage)


  