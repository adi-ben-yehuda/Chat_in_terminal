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
    joinMessage = myName + ' has joined'

    for i in range(0, len(dictMembers)):
        key = (str)(list(dictMembers.keys())[i])
        if (key != myName):
          (dictMessages[key]).append(str.encode(joinMessage))      


## Change the name of a member in the group to a new name
def changeName(address, newName):
  newName = newName.split()[1]

  ## Change the name from dictionary members
  dictMembers[newName] = address
  oldName = list(dictMembers.keys())[list(dictMembers.values()).index(address)]
  del dictMembers[oldName]

  ## Change the name from dictionary messages
  dictMessages[newName] = dictMessages[oldName]
  del dictMessages[oldName]

  ## Send a message to all the members that that someone changed his name
  changeMessage = oldName + ' changed his name to ' + newName

  for i in range(0, len(dictMembers)):
      key = (str)(list(dictMembers.keys())[i])
      if (key != newName):
        (dictMessages[key]).append(str.encode(changeMessage)) 

  s.sendto(b'', address)


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
dictMessages = {}

while True:
    data, addr = s.recvfrom(1024)
    if ((str)(data) != "b''"):
      dataStr = data.decode("utf-8")
      num,dataMessage = dataStr.split(' ', 1)
      if (num == '1'):
        addToGroup(addr, dataMessage)
      if (num == '2'):
        sendMessage(addr,dataMessage)
      if (num == '3'):
        changeName(addr, dataStr)
    
    print(dictMembers)
    print(dictMessage)


  