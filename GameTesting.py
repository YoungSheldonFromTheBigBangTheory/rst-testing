#python3 -m pip install --upgrade termcolor
import sys, random, time
from termcolor import colored, cprint
from Inventory import *

uba = False
pos = float(0)
tempOpt:list = []
tempPos:list = []
reqdItem:list = []
tempItem:list = []
Inventory.inventory.append(Items.Dime)

wpmR = 125 #Regular print speed
wpmF = 600 #Fast print speed
wpm = wpmR #wpm

def Type(t): #Word typing control
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/wpm)

def viewInventory():
    print("--------------------------------------\n")
    for item in Inventory.inventory:
        item:Item
        Type(item.Name)
        print("")
    print("\n--------------------------------------\n")

def Interact(): #Balls

    for i in range(0, len(tempOpt)):
        Type(str(i + 1))
        Type(")")
        Type(str(tempOpt[i]))
        print("")

    while True:

        temp = input("⇥   ").lower()

        if temp == "give items":
            Inventory.inventory.append(Items.HouseKey)
            Inventory.inventory.append(Items.NightStandKey)
            Inventory.inventory.append(Items.BobbyPin)
            Inventory.inventory.append(Items.FlashLight)
            print("given items")

        if temp == "i" or temp == "inventory":
            viewInventory()

        for item in Inventory.inventory:
            item:Item
            for i in range(0, len(tempPos)): #Range of 0 to list
                if temp == str(i+1) and tempPos[i] != "null": #Compare if input is equal to list
                    if item.Check(reqdItem[i]) is True or reqdItem[i] == Items.Null:
                        pos = tempPos[i]
                        return pos
                
        if temp != "i" and temp != "inventory": 
            Type("\nYou lack the required item... \n\n")

def pickUp():
    global pos
    opt:list = []
    itm:list = []
    for i in range(0, len(tempOpt)):
        if tempOpt[i] != "null":
            prb:list = []
            for item in Inventory.inventory:
                item:Item
                if item.Check(tempItem[i]) is True:
                    prb.append(True)
            if not any(prb):
                opt.append(tempOpt[i])
                itm.append(tempItem[i])
    for num, letter in enumerate(opt):
        Type(str(num + 1))
        Type(")")
        Type(letter)
        print("")

    temp = input("⇥   ")

    if temp == "i" or temp == "inventory":
            
        viewInventory()

    for i in range(0, len(opt)):
        if temp == str(i+1) and tempItem[i] != Items.Null:
            Inventory.inventory.append(itm[i])
            if itm[i] is not Items.Return:
                print("--------------------------------------\n")
                Type("You obtained a ")
                print(itm[i].Name)
                print("\n--------------------------------------\n")


    for item in Inventory.inventory:
        item:Item
        if item.Check(Items.Return) is True:
            Inventory.inventory.remove(Items.Return)
            pos = tempPos[0]

        
while True: #Start Game
    Type("Options are selected using numbers 1-4\nTo view inventory type inventory or i\n")
    temp = input("start game? y/n: ").lower()

    if temp == "yes" or temp == "y":
        break
    elif temp == "no" or temp == "n":
        sys.exit("Ok then")
    Type("Um what?")

while True: #Pos 0

    if pos == 0: #Spawn
        Type("You find yourself on a rocky path in front of a slightly weathered, red bricked house\n")
        tempOpt = ["Walk inside", "Continue path left", "Continue path right"]
        tempPos = [1, 2, 3, "null"]
        reqdItem = [Items.HouseKey, Items.Null, Items.Null, Items.Null]
        pos = Interact()

    if True: #Inside house

        if pos == 1: #House Entrance
            Type("You find yourself in the entrance of the house\n")
            tempOpt = ["Head upstairs", "Head straight towards kitchen", "Turn right to the living room", "Exit the house"]
            tempPos = [1.2, 1.11, 1.12, 0]
            reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
            pos = Interact()
        if True: #Kitchen
            if pos == 1.11: #Kitchen
                Type("You step onto the black & white checkered floor. Close beside you to your left is a line of smooth white cabinets. \n")
                tempOpt = ["Search cabinet", "Search drawer", "Turn right to the living room", "Return to entrance"]
                tempPos = [1.111, 1.112, 1.12, 1]
                reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                pos = Interact()
            if pos == 1.111: #Kitchen cabinet
                Type("You open the cabinet. There is nothing.\n")
                tempOpt = ["Return"]
                tempPos = [1.11, "null", "null", "null"]
                reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                pos = Interact()
            if pos == 1.112: #Kitchen drawer 
                Type("You pull open the drawer and peer inside. \n")
                tempOpt = ["Take spoon", "Take canned beans", "Take small key", "Return"]
                tempItem = [Items.Spoon, Items.Beans, Items.NightStandKey, Items.Return]
                tempPos = [1.11, "null", "null", "null"]
                reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                pickUp()

        if True: #upstairs
            if pos == 1.2:
                Type("You stand a top the stairs\n")
                tempOpt = ["Continue down the hall", "Turn into bathroom", "Go down stairs"]
                tempPos = [1.22, 1.21, 1, "null"]
                reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                pos = Interact()

        if True: #upstair bathroom
            if pos == 1.21:
                Type("You see a counter with three drawers\n")
                tempOpt = ["Search top drawer", "Search middle drawer", "Search bottom drawer", "Return to hall"]
                tempPos = [1.211, 1.212, 1.213, 1.2]
                reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                pos = Interact()
            if True: #Upstairs bathroom drawers
                if pos == 1.211:
                    Type("You pull open the top drawer and peer inside. \n")
                    tempOpt = ["Take tooth brush", "Return", "null", "null"]
                    tempItem = [Items.ToothBrush, Items.Return, Items.Null, Items.Null]
                    tempPos = [1.21, "null", "null", "null"]
                    reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                    pickUp()
                if pos == 1.212:
                    Type("You pull open the middle drawer and peer inside. You see nothing\n")
                    tempOpt = ["Return"]
                    tempPos = [1.21, "null", "null", "null"]
                    reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                    pos = Interact()
                if pos == 1.213:
                    Type("You pull open the bottom drawer and peer inside. \n")
                    tempOpt = ["Take Q-tip", "Take bobby pin", "Return", "null"]
                    tempItem = [Items.QTip, Items.BobbyPin, Items.Return, Items.Null]
                    tempPos = [1.21, "null", "null", "null"]
                    reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                    pickUp()


        if True: #Upstairs bedroom(entrance)
            if pos == 1.22 and uba == False:#Bedroom entrance(closed)
                Type("You stand before a large door. \n")
                tempOpt = ["Pick lock", "Return to stairs"]
                tempPos = [1.221, 1.2, "null", "null"]
                reqdItem = [Items.BobbyPin, Items.Null, Items.Null, Items.Null] 
                pos = Interact()
            if pos == 1.22 and uba == True: #Bedroom entrance(open)
                Type("You stand before a large open door. \n")
                tempOpt = ["Enter", "Return to stairs"]
                tempPos = [1.221, 1.2, "null", "null"]
                reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                pos = Interact()

            if pos == 1.221: #inside bedroom
                uba = True
                Type("You are in a large, hardwood floored room with a tall ceiling  \n")
                tempOpt = ["Look out window", "Search dresser", "Search night stand", "Return outside bedroom"]
                tempPos = [1.2211, 1.2212, 1.2213, 1.22]
                reqdItem = [Items.Null, Items.Null, Items.NightStandKey, Items.Null] 
                pos = Interact()
            if True:
                if pos == 1.2211:
                    Type("You look outside the window. It is dark but you make out the faint outlines of trees. \n")
                    tempOpt = ["Return"]
                    tempPos = [1.221, "null", "null", "null"]
                    reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                    pos = Interact()
                if pos == 1.2212:
                    Type("You open the dresser and look inside. You see cloths old clothes but nothing of value. \n")
                    tempOpt = ["Return"]
                    tempPos = [1.221, "null", "null", "null"]
                    reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                    pos = Interact()
                if pos == 1.2213:
                    Type("You open the drawer of the night stand. \n")
                    tempOpt = ["Take Flashlight","Return","null","null"]
                    tempItem = [Items.FlashLight, Items.Return, Items.Null, Items.Null]
                    tempPos = [1.221, "null", "null", "null"]
                    reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                    pickUp()

        if True: #Living Room
            if pos == 1.12: #Living Room
                Type("The hard wood creaks below you as you enter the living room. \n")
                tempOpt = ["Look outside", "Go to kitchen", "Return to entrance"]
                tempPos = [1.121, 1.11, 1, "null"]
                reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
                pos = Interact()
            if pos == 1.121: #Living Room Window
                Type("You aproach the window and look outside. It is dark. You see the faint outlines of trees\n")
                tempOpt = ["Return"]
                tempPos = [1.12, "null", "null", "null"]
                reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null]
                pos = Interact()

    if True: #Path left
        if pos == 2:
            Type("You stand before a guiled chest\n")
            tempOpt = ["Search", "Return"]
            tempPos = [2.1, 0, "null", "null"]
            reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null]
            pos = Interact()

        if pos == 2.1:
            Type("You peer into the chest\n")
            tempOpt = ["Take key", "Take gold coin", "Return", "null"]
            tempItem = [Items.HouseKey, Items.GoldCoin, Items.Return, Items.Null]
            tempPos = [2, "null", "null", "null"]
            reqdItem = [Items.Null, Items.Null, Items.Null, Items.Null] 
            pickUp()

    if True: #Path right
        if pos == 3:
            Type("You look into the dense, dark tree line\n")
            tempOpt = ["Continue", "Return"]
            tempPos = [3.1, 0, "null", "null"]
            reqdItem = [Items.FlashLight, Items.Null, Items.Null, Items.Null]
            pos = Interact()
        if pos == 3.1:
            Type("Thank you for playing the game")
            sys.exit()
