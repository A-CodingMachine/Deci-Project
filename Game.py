import random
import time
import numpy as n
#Functions are mostly ordered alphebetically

#Preparing some variables
NumberFail = "Press 1 or 2 "
CharacterFail = "Press y or n "

PlayerAttributes = { #Using dictionaries for scores and attributes 
    "Score" : 0,     # Plus uses a concept of OOP so why not
    "Thirsty" : True,
    "HasAxe" : False,
    "Health": 100
}
MaskedAttributes = {
  "Health":100,
  "Dizzy": False,
  "RoundDizzyFor":0
 }

def PrintPause(Text): #Just a normal printpause function
    print(Text)
    time.sleep(2)

def IncreaseScore(Amount = float): #increase scores easily plus print text
    global PlayerAttributes
    PlayerAttributes["Score"] += Amount
    PrintPause("You score has increased by " + str(Amount))
    PrintPause("Your current score: " + str(PlayerAttributes["Score"]))

def ResetBattle(): #Continueing the while loop also allow for returning back to menu in future updates
    global MaskedAttributes
    global PlayerAttributes


    if MaskedAttributes["Dizzy"] and MaskedAttributes["RoundDizzyFor"] < 2:
        MaskedAttributes["RoundDizzyFor"] += 1
    else:
        MaskedAttributes["Dizzy"] = False
        MaskedAttributes["RoundDizzyFor"] = 0


    PrintPause("""
            ///////////// \n
          //////////////// \n
         /// -- //// -- /// \n
         ////////////////// \n
          ////       //// \n
           ///////////// \n
           """)
    Choice = CheckChoiceViability("[1] Fight [2] Action [3] Info", ["1", "2", "3"], "1 or 2 or 3")
    if Choice == "1":

        PrintPause("You have attacked the mask")

        if random.randint(1,4) == 4:
            PrintPause("The masked dodged")
            return
  
        PrintPause("Your attack succeded!")
        if PlayerAttributes["HasAxe"]: MaskedAttributes["Health"] -= 60 
        else: MaskedAttributes["Health"] -= 10
        print("The masked health is ", MaskedAttributes["Health"])
  
    elif Choice == "2":

        Choice = CheckChoiceViability("[1] Shout [2] Steal axe", ["1", "2"], "1 or 2 please ")
        if Choice == "1":
            PrintPause("Your shout causes the Masked to feel dizzy")
            MaskedAttributes["Dizzy"] = True
        else:
            if PlayerAttributes["HasAxe"]: 
                PrintPause("You already have an axe")
            elif MaskedAttributes["Dizzy"] == False:
                PrintPause("The masked slashes")
                PrintPause("You failed to take the axe")
                PrintPause("You lost 10 hp")
                PlayerAttributes["Health"] -= 10
                PrintPause("Your current health is" + str(PlayerAttributes["Health"]))


    else:
        PrintPause("The masked health is " + str(MaskedAttributes["Health"]))
        PrintPause("Your health is " +  str(PlayerAttributes["Health"]))
        PrintPause("Your score is " +  str(PlayerAttributes["Score"]))
        ResetBattle()
 

#Battle function
def Battle():
    global PlayerAttributes
    global MaskedAttributes
 
    while PlayerAttributes["Health"] > 0 and MaskedAttributes["Health"] > 0:
        ResetBattle()
        PrintPause("The Masked attempts to attack")
        if MaskedAttributes["Dizzy"]:
            PrintPause("The Masked is way too dizzy to attack")
            PrintPause("You managed to dodge his attack")
        else:
            PrintPause("The masked slashes you with his axe")
            PrintPause("You've lost 50 HP")
            PlayerAttributes["Health"] -= 50
            PlayerAttributes["Health"] = n.clip(PlayerAttributes["Health"], 0, 100)
            print("Your health: ", PlayerAttributes["Health"])

    if PlayerAttributes["Health"] <= 0:
        PrintPause("You have died...")


def CheckChoiceViability(Text, ViableChoices, FailedText = None): #Check choices and make sure they are correct
    Choice = input(Text + "\n")                                      #You can also add a custom failed text if you want

    if ViableChoices == "any":
        return Choice

    while not Choice in ViableChoices: #While loop to make sure Choice is viable
        print("not valid input...")
        Choice = input(FailedText or Text + "\n")
 
    return Choice

 



#Orginizing the room choices into function
def InclosedRoomFirstChoice():
    PrintPause("You found a lock")
    Choice = CheckChoiceViability("[1] Try to picklock [2] leave it alone", ["1", "2"], "1 or 2")
    if Choice == "1":
        PrintPause("you have been electrocuted")
        PrintPause("You died..")
    else:
        PrintPause("You continue to wait in your room not knowing what to do..")
        PrintPause("You have always been a loner")
        PrintPause("No friends, most family died besides your grandma")
        PrintPause("You're making barely minimum wage and...")
        PrintPause("You feel sad, depressed")
        PrintPause("You feel like you shouldve done better")
        PrintPause("Your scared, scared of dying alone")
        PrintPause("Tears start dropping from your eyes")
        PrintPause("You start remenescing..")
        PrintPause("you wait...")
        PrintPause("and wait...")
        PrintPause("and wait..")
        PrintPause("To be continued..")


def InclosedRoomSecondChoice(): #Second room choice basically
    global PlayerAttributes #Where you can fight and do other things

    PrintPause("You hear a weird noise")
    PrintPause("A man enters the room")
    PrintPause("He is MASKED")
    PrintPause("The masked tries to attack")
    PrintPause("You try to dodge")

    if PlayerAttributes["Thirsty"]:
        PrintPause("You are too dehydrated, the masked man slashes you...")
        PrintPause("You died...")
        return
    else:
        PrintPause("You were able to dodge")
        PrintPause("Nice dodge")
        IncreaseScore(20)
        Choice = CheckChoiceViability("[1] Shout, [2] Run away, [3] Fight", ["1", "2", "3"])
        if Choice == "1":

            PrintPause("The masked feels DIZZY")
            PrintPause("You were able to exit the room and run past him")
            PrintPause("You continue running till you reach another exit")
            PrintPause("You managed to escape but where are you?")
            PrintPause("To be continued")
            return
        elif Choice == "2":
            PrintPause("The masked is able to slash you...")
            PrintPause("You died...")
            return
        elif Choice == "3":
            return True


def InclosedRoomThirdChoice(): #Room third choice
    #Nothing much just doing some storytelling
    PrintPause("You continue to sleep for a while...")
    PrintPause("You were slashed while sleeping..")
    PrintPause("You died...")
    return

#Main game function
def Game():
    global PlayerAttributes
    
    PrintPause("MASKED \n __________________")
    CheckChoiceViability("Press any button to start", "any")

    PrintPause("You feel thirsty...")
    PrintPause("There is a water bottle next to you")
    Choice = CheckChoiceViability("Drink from the bottle? Press 1 to drink or 2 not to", ["1", "2"], NumberFail)

    #Water botlle gameplay plus introducing randomisation mechanic
    if Choice == "1":
        Die = random.randint(1,3) == 3 #Using randomization to add more custom gameplay
        if Die:
            PrintPause("You have been poisoned!")
            PrintPause("You died..")
            return
        else:
            PlayerAttributes["Thirsty"] = False
            PrintPause("You feel refreshed")
            PrintPause("Good for you!")
            IncreaseScore(10)
    else:
        print("You still feel thirsty")
        PlayerAttributes["Thirsty"] = True
   
    PrintPause("It looks like your in an inclosed room with large metal walls")
    PrintPause("What do you do?")

    #Inclosed room gameplay
    Choice = CheckChoiceViability(""" 
    [1] check the door of the room,
    [2] stay on your bed,
    [3] sleep?""", ["1", "2", "3"], "Choose 1 or 2 or 3")

    if Choice == "1":
        InclosedRoomFirstChoice()
        return
    elif Choice == "2":
        Fight = InclosedRoomSecondChoice()
        if Fight == True:
            Battle()
            return
    else:
        InclosedRoomThirdChoice()
    

while True:
    Game()
    print("You final score is ", PlayerAttributes["Score"])
    Choice = CheckChoiceViability("Do you want to play again Y/N ", ["Y", "N", "y", "n"], CharacterFail)
    
    if Choice.capitalize() == "N":
        break
    
    PlayerAttributes["Score"] = 0
    PlayerAttributes["Thirsty"] = True

