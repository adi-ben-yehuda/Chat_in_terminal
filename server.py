import socket
import sys

 ## Add member to the group
def addToGroup(address, data):
  myName = (str)(data).split(' ', 1)
  
  ## Check if the name is already in the group
  if (myName[1] not in dictMembers):
    myName = myName[1]
    ## Add the member to the group
    dictMembers[myName] = address
    dictMessages[myName] = []
    
    ## Send to the client all the members in the group
    if (len(dictMembers) > 1):
      groupNames = (str)(list(dictMembers.keys())[len(dictMembers) - 2]) 
      for i in reversed(range(len(dictMembers) - 2)):
        key = (str)(list(dictMembers.keys())[i])
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
  else:
    s.sendto(b'Illegal request', address)


## Change the name of a member in the group to a new name
def changeName(address, newName):  
  newName = newName.split(' ', 1)
  
  ## If the client send only number without name
  if (len(newName) == 1):
    s.sendto(b'Illegal request', address)
  else:
    newName = newName[1]
    ## Change the name from dictionary members
    dictMembers[newName] = address
    oldName = list(dictMembers.keys())[list(dictMembers.values()).index(address)]
    del dictMembers[oldName]

    ## Change the name from dictionary messages
    dictMessages[newName] = dictMessages[oldName]
    del dictMessages[oldName]

    ## Send a message to all the members that someone changed his name
    changeMessage = oldName + ' changed his name to ' + newName

    ## Add the message to the dictionry of messages to everyone in the group
    for i in range(0, len(dictMembers)):
        key = (str)(list(dictMembers.keys())[i])
        if (key != newName):
          (dictMessages[key]).append(str.encode(changeMessage)) 

    s.sendto(b'', address)


## Send a message to all the members
def sendMessage(addr, dataMessage):
  text = (str)(dataMessage).split(' ', 1)
  
  ## If the client send only number without name
  if (len(text) == 1):
    s.sendto(b'Illegal request', addr)
  else:
     ## Get the name of the client that send the message
    nameOfSend = list(dictMembers.keys())[list(dictMembers.values()).index(addr)]
    text = text[1]
    ## The message to send all the members that in the group
    sendMessage = (str)(nameOfSend) + ': ' + text
    
    ## Add the message to the dictionry of messages to everyone in the group
    for i in range(0, len(dictMembers)):
        key = (str)(list(dictMembers.keys())[i])
        if (key != (str)(nameOfSend)): 
          (dictMessages[key]).append(str.encode(sendMessage))
    s.sendto(b'', addr)


## Delete member from the group
def leaveGroup(addr):
  ## Get the name of the cliet that send the message
  nameOfSend = list(dictMembers.keys())[list(dictMembers.values()).index(addr)]  

  ## The message to send all the members that in the group
  leftMessage = (str)(nameOfSend)  + ' has left the group'

  ## Remove the member
  del dictMembers[nameOfSend]
  del dictMessages[nameOfSend]
  
  ## Add the message to the dictionry of messages to everyone in the group
  for i in range(0, len(dictMembers)):
      key = (str)(list(dictMembers.keys())[i])
      if (key != (str)(nameOfSend)):
        (dictMessages[key]).append(str.encode(leftMessage))
  s.sendto(b'close', addr)


## Send updates to the member when asked
def getUpdate(addr):

  ## Get the name of the cliet that send the message
  nameOfSend = list(dictMembers.keys())[list(dictMembers.values()).index(addr)]

  numOfUpdates = len(dictMessages[nameOfSend])  
  s.sendto(str.encode((str)(numOfUpdates)), addr)

  ## Send all the updates to the member
  for i in range(0, numOfUpdates):
    updates = dictMessages[nameOfSend][i]
    s.sendto(updates, addr)
  dictMessages[nameOfSend] = []


## Check if the member exists in the dictionary
def checkIfMemberExists(adress):
  if adress in dictMembers.values():
    return True
  else:
    return False

## Check if the data is valid
def checkIfDataIsValid(data, addr):
  text = (str)(data).split(' ', 1)
  
  ## If the client send not only a number
  if (len(text) != 1):
    s.sendto(b'Illegal request', addr)
    return False
  else:
    return True

## Check if the name is not empty or includes only spaces or is numeric
def checkIfDataIsName(data, addr):
  name = (str)(data).split(' ', 1)
  ## If the client send only number without name
  if (len(name) == 1):
    s.sendto(b'Illegal request', addr)
  elif (len(name[1]) == 0 or name[1][0] == ' ' or name[1].isnumeric()):
    s.sendto(b'Illegal request', addr)
    return False
  else:
    return True

## Check if message is not empty or includes only spaces
def checkIfDataIsNotEmpty(data, addr):
  name = (str)(data).split(' ', 1)
  ## If the client send only number without text
  if (len(name) == 1):
    s.sendto(b'Illegal request', addr)
  elif (len(name[1]) == 0 or name[1].isspace()):
    s.sendto(b'Illegal request', addr)
    return False
  else:
    return True
  

## Get data from the command line and check if valid.
args = sys.argv
##args = ["djkdkd", "12345"]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if(len(args) == 2 and args[1].isnumeric() and (int)(args[1]) in range(0, 65535)):
  port = (int)(args[1])
  s.bind(('', port))
  dictMembers = {}
  dictMessages = {}

  ## Get the data from the client and act according to his request
  while True:
      data, addr = s.recvfrom(1024)
      ## When the user press enter
      if ((str)(data) != "b''"):
        dataStr = data.decode("utf-8")
        ## When the data is only spaces
        if (dataStr.isspace()):
          s.sendto(b'Illegal request', addr)
        else:
          num = (str)(dataStr).split()[0]
          if (num == '1'):
            if(checkIfDataIsName(dataStr, addr)):
              addToGroup(addr, dataStr)
          elif (checkIfMemberExists(addr)):
              if (num == '2'):
                if(checkIfDataIsNotEmpty(dataStr, addr)):
                  sendMessage(addr,dataStr)
              elif (num == '3'):
                if(checkIfDataIsName(dataStr, addr)):
                  changeName(addr, dataStr)
              elif (num == '4'):
                if (checkIfDataIsValid(dataStr, addr)):
                  leaveGroup(addr)
              elif (num == '5'):
                if (checkIfDataIsValid(dataStr, addr)):
                  getUpdate(addr)
              else:
                s.sendto(b'Illegal request', addr)
          else:
            s.sendto(b'Illegal request', addr)
      else:
        s.sendto(b'Illegal request', addr)
else:
  s.close()