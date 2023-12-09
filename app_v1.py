import os
import json

def loadEventData():
 file = open("data/event.json")
 data = json.load(file)
 return data

def printEvent(data):
 print("#" * 30)
 print(f"Event: {data['title']}")
 print(f"Date: {data['date']}")
 print(f"Guests: {len(data['guests'])}")
 print("#" * 30)

def showGuests(data):
 for i in range(len(data["guests"])):
  print(f"{i}. {data['guests'][i]}")
 #input("press enter to return to menu")

def inviteGuest(data):
 name = input("Enter guest name: ")
 data["guests"].append(name)
 return data
 
def saveData(data):
 file = open("data/event.json", "w")
 data = json.dump(data, file)
 file.close()
 
def inviteanotherGuest(data):
 name = input("Invite another guest or press enter to return to menu: ")
 if name == "":
  return
 else:
  data["guests"].append(name)
  saveData(data)
  inviteanotherGuest(data)


# hm1: while/for + menu + interactive + remove
# hm2: upload to github
# data = loadEventData()
# printEvent(data)
# data = inviteGuest(data)
# printEvent(data)
# saveData(data)

while True:
# interaction
 os.system("clear")
 data = loadEventData()
 printEvent(data)
 print("*** menu ***\n1. invite a gest\n2. remove guest\n3. clear guest list\n0. exit\n")
 showGuests(data)
 item = int(input())
 if item == 1:
  saveData(inviteGuest(data))
  inviteanotherGuest(data)
 elif item == 2:
  pos = input("hit enter to cancel\nenter guest position to remove: ")
  if pos == "":
   continue
  else:
   data["guests"].pop(int(pos))
   saveData(data)
 elif item == 3:
  data["guests"].clear()
  saveData(data)
 elif item == 0:
  break