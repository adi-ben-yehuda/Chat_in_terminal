import socket
import sys

def addToGroup(address, name):
  
  if name not in dict:
    ## Add the member to the group
    myName = (str)(name).split()[1].split("'")[0]
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
port = (int)(args[1])
s.bind(('', port))
dict = {}


while True:
    data, addr = s.recvfrom(1024)
    print(data)
    if (data.decode("utf-8") != "b''"):
      num = (str)(data.split()[0]).split("'")[1]
      if (num == '1'):
        addToGroup(addr, str(data))
      
      print(dict)


  