import time
import sys
import os
#Player Stats
name = ''
hp = 50
amr = 5
attdmg = 5
mgcdmg = 5
gold = 0
mgcskl = 0
attskl = 0
wpnname = ''
amrname = ''
potions = ['Health Potions: ', 0 , 'Mana Potions: ', 0 , 'Escape Potions: ', 0]
mobname = ''
mobamr = 0
mobatt = 0
mobhp = 0
plrtrn = True

def mainMenu():

    print ("Wham's Adventure Game")
    print ('--------------------')
    print ('1) New Game')
    print ('2) Load Game')
    print ('3) Credits')
    print ('--------------------')
    
    choice = input()
    if (choice == '1'):
        NewGame()
    elif(choice == '2'):
        loadGame()
    else:
        mainMenu()

def NewGame():
    global name
    print ('New game selected')
    name = input('Please enter your name: ')
    welcomeMsg = ('Welcome '+name+', are you ready to start your adventure?')
    speak(welcomeMsg)
    print('')
    global wpnname
    global amrname
    global gold
    wpnname = 'Rusty Sword'
    amrname = 'Rusty Armour'
    gold = 0
    mainGameMenu()

def mainGameMenu():
    print ('--------------------')
    print ('1) Random Dungeon')
    print ('2) Story')
    print ('3) Shop')
    print ('4) Magic Talent Tree')
    print ('5) Save Game ')
    print ('6) Quit Game ')
    print ('--------------------')
    choice = input()
    if (choice == '1'):
        randomDungeon()
    elif(choice == '2'):
        story()
    elif(choice == '3'):
        shopMain()
    elif(choice =='4'):
        magicSkills()
    elif(choice =='5'):
        saveGame()
    elif(choice == '6'):
        quitGame()
    else:
        mainGameMenu()

def randomDungeon():
    dung = 1
    if (dung == 1):
        result = crabAttack()
        if (result == True):
            speak('Event Completed!')
        else:
            speak('Event Avoided!')
    else:
        print('')
    
    input('Press any key to continue')
    mainGameMenu()

    
def story():
    #Story mode?
    print('')
    
def shopMain():
    global name
    print ('--------------------')
    shopmsg = ('Welcome '+name+', What do you need?')
    speak(shopmsg)
    print ('--------------------')
    print ('1) Weapon Shop')
    print ('2) Armour Shop')
    print ('3) Potions')
    print ('4) Leave Shop')
    print ('--------------------')
    choice = input()
    if (choice == '1'):
        weaponShop()
    elif(choice == '2'):
        armourShop()
    elif(choice == '3'):
        potionsShop()
    elif(choice == '4'):
        mainGameMenu()
    else:
        shopMain()
        
def weaponShop():
    print ('--------------------')
    print ('1) Iron Sword | Dmg: 15 | 200g')
    print ('2) Steel Sword | Dmg: 45 | 500g')
    print ('3) Elven Sword | Dmg: 80 | 1,000g')
    print ('4) Leave Shop')
    print ('--------------------')
    print ('Your Current Weapon:')
    print (wpnname+' | Dmg: '+str(attdmg))
    print ('--------------------')
    choice = input()
    if (choice == '1'):
        tryBuy('Iron Sword', 200, 'wpn', 15)
    elif(choice == '2'):
        tryBuy('Steel Sword', 500, 'wpn', 45)
    elif(choice == '3'):
        tryBuy('Elven Sword', 1000, 'wpn', 80)
    elif(choice == '4'):
        mainGameMenu()
    else:
        shopMain()
        
def armourShop():
    print ('--------------------')
    print ('1) Iron Armour | Amr: 15 | 200g')
    print ('2) Steel Armour | Amr: 45 | 500g')
    print ('3) Elven Armour | Amr: 80 | 1,000g')
    print ('4) Leave Shop')
    print ('--------------------')
    print ('Your Current Armour:')
    print (amrname+' | Amr: '+str(amr))
    print ('--------------------')
    choice = input()
    if (choice == '1'):
        tryBuy('Iron Armour', 200, 'amr', 15)
    elif(choice == '2'):
        tryBuy('Steel Armour', 500, 'amr', 45)
    elif(choice == '3'):
        tryBuy('Elven Armour', 1000, 'amr', 80)
    elif(choice == '4'):
        mainGameMenu()
    else:
        shopMain()
        
def potionsShop():
    print ('--------------------')
    print ('1) Health Potion | 50g')
    print ('2) Mana Potion | 50g')
    print ('3) Escape Potion | 100g')
    print ('4) Leave Shop')
    print ('--------------------')
    print ('Your Current Potion Inventory:')
    print (potions)
    print ('--------------------')
    choice = input()
    if (choice == '1'):
        tryBuy('Health Potion', 50, 'ptn', 'h')
    elif(choice == '2'):
        tryBuy('Mana Potion', 50, 'ptn', 'm')
    elif(choice == '3'):
        tryBuy('Escape Potion', 100, 'ptn', 'e')
    elif(choice == '4'):
        mainGameMenu()
    else:
        shopMain()
        
def magicSkills():
    print('')
    
def tryBuy(newItemName, cost, ItemType, rtn):
    global gold
    global wpnname
    global potions
    global amrname
    global attdmg
    global amr
    if (gold > cost):
        gold = gold - cost
        if (ItemType == 'amr'):
            itmmsg = (newItemName+" is now your current armour!")
            speak(itmmsg)
            amrname = newItemName
            amr = rtn
            shopMain()
        if (ItemType == 'wpn'):
            itmmsg = (newItemName+" is now your current weapon!")
            speak(itmmsg)
            wpnname = newItemName
            attdmg = rtn
            shopMain()
        if (ItemType == 'ptn'):
            itemmsg = (newItemName+ ' is now in your inventory')
            speak(itmmsg)
            if (rtn == 'h'):
                potions[1] = potions[1] + 1
            elif (rtn == 'm'):
                potions[3] = potions[3] + 1
            elif (rtn == 'e'):
                potions[5] = potions[5] + 1
            shopMain()
    else:
        nogoldmsg = ('Not enough gold!')
        speak(nogoldmsg)
        shopMain()
        
def saveGame():
    global name
    global hp
    global amr
    global attdmg
    global mgcdmg
    global gold
    global mgcskl
    global attskl
    global wpnname
    global amrname
    global potions
    f = open("savegame", "w")
    f.write(name+'\n'+str(hp)+'\n'+str(amr)+'\n'+str(attdmg)+'\n'+str(mgcdmg)+'\n'+str(gold)+'\n'+str(mgcskl)+'\n'+str(attskl)+'\n'+wpnname+'\n'+amrname+'\n'+str(potions[1])+'\n'+str(potions[3])+'\n'+str(potions[5]))
    print('Save Succesful')
    mainGameMenu()

def loadGame():
    global name
    global hp
    global amr
    global attdmg
    global mgcdmg
    global gold
    global mgcskl
    global attskl
    global wpnname
    global amrname
    global potions
    f = open("savegame", "r")
    name = (f.readline())
    name = name[:-1]
    hp = int((f.readline()))
    amr = int((f.readline()))
    attdmg = int((f.readline()))
    mgcdmg = int((f.readline()))
    gold = int((f.readline()))
    mgcskl = int((f.readline()))
    attskl = int((f.readline()))
    wpnname = (f.readline())
    wpnname = wpnname[:-1]
    amrname = (f.readline())
    amrname = amrname[:-1]
    potions[1] = int((f.readline()))
    potions[3] = int((f.readline()))
    potions[5] = int((f.readline()))
    mainGameMenu()

def speak(msg):
    for char in msg:
        print(char, end='')
        time.sleep(.01)
    print('')
    return
def quitGame():
    exit

############### EVENTS #######################################

def crabAttack():
    speak('While walking down the road you see a man approach')
    speak('He seems scared and speaks to you')
    speak('Help me! A large crab has stolen my coin purse!')
    speak("Please get it back for me, I will reward you for your efforts!")
    speak(name+', do you go to help the man? Yes or No ')
    des = input('')
    if (des == 'Yes') or (des == 'yes') or (des == 'y'):
        speak('You follow the man to the crab')
        speak('You approach the Large Crab and prepare to fight!')
        battle('Large Crab', 10,1, 10)
        speak('Thank you for helping me! This is for your service!')
        speak('You received 5 gold!')
        return True
    elif (des == 'No') or (des == 'no') or (des == 'n'):
        speak("I don't blame you! It's huge! Watch out for more on your journey!")
        return False
    else:
        speak('Your response confuses the man and he backs away slowly from you')
        return False
    
def battle(emobname, emobhp, emobamr, emobatt):
    global name
    global hp
    global amr
    global attdmg
    global mgcdmg
    global gold
    global mgcskl
    global attskl
    global wpnname
    global amrname
    global potions
    global mobname
    global mobamr
    global mobatt
    global mobhp
    global plrtrn
    mobname = emobname
    mobamr = emobamr
    mobatt = emobatt
    mobhp = emobhp
    while (mobhp > 0) and (plrtrn == True):
        print ('--------------------')
        print (name+' Health: '+str(hp))
        print (mobname+' Health: '+str(mobhp))
        print ('1) Attack with your '+wpnname)
        print ('2) Use a spell')
        print ('3) Use a Potion')
        print ('--------------------')
        choice = input()
        if (choice == '1'):
            attdmghit = attdmg - mobamr
            mobhp = mobhp - attdmghit
            speak('You hit the '+mobname+' for '+str(attdmghit)+'!')
            plrtrn = False
        elif (choice == '2'):
            print ('1) Damage Spell')
            print ('2) Heal Spell')
            choice = input()
            if (choice == '1'):
                hp = hp + mgcskl
                plrtrn = False
            elif (choice == '2'):
                mobhp = mobhp - mgcskl
                plrtrn = False
            else:
                battle(mobname, mobhp, mobamr, mobatt)
        elif (choice == '3'):
            print ('1) Health Potion | '+potions[1])
            print ('2) Mana Potion | '+potions[3])
            print ('3) Escape Potion | '+potions[5])
            choice = input()
            if (choice == '1'):
                if (potions[1] > 0):
                    hp = hp + 20
                    plrtrn = False
                else:
                    speak('No health potions available!')
                    battle(mobname, mobhp, mobamr, mobatt) 
            if (choice == '1'):
                if (potions[1] > 0):
                    hp = hp + 20
                    plrtrn = False
                else:
                    speak('No health potions available!')
                    battle(mobname, mobhp, mobamr, mobatt) 
            if (choice == '1'):
                if (potions[1] > 0):
                    hp = hp + 20
                    plrtrn = False
                else:
                    speak('No health potions available!')
                    battle(mobname, mobhp, mobamr, mobatt) 
            else:
                battle(mobname, mobhp, mobamr, mobatt)                
        else:
            battle(mobname, mobhp, mobamr, mobatt)
    while (mobhp > 0) and (plrtrn == False):
        mobatthit = mobatt - amr
        hp = hp - mobatthit
        plrtrn = True
        battle(mobname, mobhp, mobamr, mobatt)
    return

mainMenu()
