import socket
import sys

 ## Add member to the group
def addToGroup(address, data):

  myName = (str)(data).split()[1]
  
  if myName not in dictMembers:
    ## Add the member to the group
    dictMembers[myName] = address
    dictMessages[myName] = []
    
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

  ## Send a message to all the members that someone changed his name
  changeMessage = oldName + ' changed his name to ' + newName

  ## add the message to the dictionry of messages to everyone in the group
  for i in range(0, len(dictMembers)):
      key = (str)(list(dictMembers.keys())[i])
      if (key != newName):
        (dictMessages[key]).append(str.encode(changeMessage)) 

  s.sendto(b'', address)


## Send a message to all the members
def sendMessage(addr, dataMessage):

  ## get the name of the cliet that send the message
  nameOfSend = list(dictMembers.keys())[list(dictMembers.values()).index(addr)]
  


  ## the message to send all the members that in the group
  sendMessage = (str)(nameOfSend) + ': ' + (str)(dataMessage).split()[1]
  
  ## add the message to the dictionry of messages to everyone in the group
  for i in range(0, len(dictMembers)):
      key = (str)(list(dictMembers.keys())[i])
      if (key != (str)(nameOfSend)): 
        (dictMessages[key]).append(str.encode(sendMessage))
  s.sendto(b'', addr)



def leaveGroup(addr):

  ## get the name of the cliet that send the message
  nameOfSend = list(dictMembers.keys())[list(dictMembers.values()).index(addr)]  

  ## the message to send all the members that in the group
  leftMessage = (str)(nameOfSend)  + ' has left the group'

  del dictMembers[nameOfSend]
  del dictMessages[nameOfSend]
  
  ## add the message to the dictionry of messages to everyone in the group
  for i in range(0, len(dictMembers)):
      key = (str)(list(dictMembers.keys())[i])
      if (key != (str)(nameOfSend)):
        (dictMessages[key]).append(str.encode(leftMessage))
  s.sendto(b'', addr)


def getUpdate(addr):

  ## get the name of the cliet that send the message
  nameOfSend = list(dictMembers.keys())[list(dictMembers.values()).index(addr)]

  ## 
  for i in range(0, len(dictMessages.values())):
    updates = (str)(dictMessages[nameOfSend][1])
    s.sendto(str.encode(updates), addr)




def checkIfMemberExists(adress):
  if adress in dictMembers.values():
    return True
  else:
    return False


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
      num = (str)(dataStr).split()[0]
      if (num == '1'):
        addToGroup(addr, dataStr)
      else:
        if (checkIfMemberExists(addr)):
          if (num == '2'):
            sendMessage(addr,dataStr)
          elif (num == '3'):
            changeName(addr, dataStr)
          elif (num == '4'):
            leaveGroup(addr)
          elif (num == '5'):
            getUpdate(addr)
          else:
            s.sendto(b'Illegal request', addr)
        else:
          s.sendto(b'Illegal request', addr)

    
    print(dictMembers)
    print(dictMessages)


  