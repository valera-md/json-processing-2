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
 input("press enter to return to menu")

def inviteGuest(data):
 name = input("Enter guest name: ")
 data["guests"].append(name)
 return data

def saveData(data):
 file = open("data/event.json", "w")
 data = json.dump(data, file)
 file.close()

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
 item = int(input("*** menu ***\n1. show all guests\n2. invite a gest\n3. remove guest\n4. clear guest list\n0. exit\n"))
 if item == 1:
  os.system("clear")
  showGuests(data)
 elif item == 2:
  saveData(inviteGuest(data))
 elif item == 3:
  pos = input("hit enter to cancel\nenter guest position to remove: ")
  if pos == "":
   continue
  else:
   data["guests"].pop(int(pos))
   saveData(data)
 elif item == 4:
  data["guests"].clear()
  saveData(data)
 elif item == 0:
  break