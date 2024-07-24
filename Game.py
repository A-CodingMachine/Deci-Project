import random
import time
import numpy as n
#Functions are order depending on frequency
#of use

#Preparing some variables
number_fail = "Press 1 or 2 "
character_fail = "Press y or n "

player_attributes = {#Using dictionaries for scores and attributes
    "Score" : 0,     #Plus uses a concept of OOP so why not
    "Thirsty" : True,
    "HasAxe" : False,
    "Health": 100
}
masked_attributes = {
  "Health":100,
  "Dizzy": False,
  "RoundDizzyFor":0
 }

#Just a normal printpause function
def print_pause(Text):
    print(Text)
    time.sleep(2)

#increase scores easily plus print text
def increase_score(Amount = float):
    global player_attributes
    player_attributes["Score"] += Amount
    print_pause("You score has increased by " + str(Amount))
    print_pause("Your current score: " + str(player_attributes["Score"]))

def print_score():
    global player_attributes
    print_pause("Your current score: " + str(player_attributes["Score"]))

#Continueing the while loop also allow for returning
#back to menu in future updates
def reset_battle():
    global masked_attributes
    global player_attributes
    MenuText = "[1] Fight [2] Action [3] Info"

    if masked_attributes["Dizzy"] and masked_attributes["RoundDizzyFor"] < 2:
        masked_attributes["RoundDizzyFor"] += 1
    else:
        masked_attributes["Dizzy"] = False
        masked_attributes["RoundDizzyFor"] = 0


    print_pause("""
            ///////////// \n
          //////////////// \n
         /// -- //// -- /// \n
         ////////////////// \n
          ////       //// \n
           ///////////// \n
           """)
    choice = check_choice(MenuText,["1", "2", "3"], "1 or 2 or 3")

    if choice == "1":

        print_pause("You have attacked the mask")

        if random.randint(1,4) == 4:
            print_pause("The masked dodged")
            return

        print_pause("Your attack succeded!")
        if player_attributes["HasAxe"]: masked_attributes["Health"] -= 60
        else: masked_attributes["Health"] -= 10
        print("The masked health is ", masked_attributes["Health"])
        increase_score(20)

    elif choice == "2":

        choice = check_choice("[1] Shout [2] Steal axe",
                              ["1", "2"], "1 or 2 please ")
        if choice == "1":
            print_pause("Your shout causes the Masked to feel dizzy")
            masked_attributes["Dizzy"] = True
            print_score()
        else:
            if player_attributes["HasAxe"]:
                print_pause("You already have an axe")
            elif masked_attributes["Dizzy"] == False:
                print_pause("The masked slashes")
                print_pause("You failed to take the axe")
                print_pause("You lost 10 hp")
                player_attributes["Health"] -= 10
                Health = str(player_attributes["Health"])
                print_pause("Your current health is" + Health)


    else:
        print_pause("The masked health is " + str(masked_attributes["Health"]))
        print_pause("Your health is " +  str(player_attributes["Health"]))
        print_score
        reset_battle()


#Battle function
def battle():
    global player_attributes
    global masked_attributes

    while player_attributes["Health"] > 0 and masked_attributes["Health"] > 0:
        reset_battle()
        print_pause("The Masked attempts to attack")
        if masked_attributes["Dizzy"]:
            print_pause("The Masked is way too dizzy to attack")
            print_pause("You managed to dodge his attack")
            increase_score(5)
        else:
            print_pause("The masked slashes you with his axe")
            print_pause("You've lost 50 HP")
            player_attributes["Health"] -= 50
            Health = n.clip(player_attributes["Health"], 0, 100)
            player_attributes["Health"] = Health
            print("Your health: ", player_attributes["Health"])

    if player_attributes["Health"] <= 0:
        print_pause("You have died...")

#Check choices and make sure they are correct
#You can also add a custom failed text if you want
def check_choice(Text, ViableChoices, FailedText = None):
    Choice = input(Text + "\n")

    if ViableChoices == "any":
        return Choice

    #While loop to make sure Choice is viable
    while not Choice in ViableChoices:
        print("not valid input...")
        Choice = input(FailedText or Text + "\n")

    return Choice


#Orginizing the room choices into function
def inclose_room_first_choice():
    print_pause("You found a lock")
    Choice = check_choice("[1] Try to picklock [2] leave it alone",
                          ["1", "2"], "1 or 2")
    if Choice == "1":
        print_pause("you have been electrocuted")
        print_pause("You died..")
    else:
        print_pause("""You continue to wait in your room
 not knowing what to do..""")
        print_pause("You have always been a loner")
        print_pause("No friends, most family died besides your grandma")
        print_pause("You're making barely minimum wage and...")
        print_pause("You feel sad, depressed")
        print_pause("You feel like you shouldve done better")
        print_pause("Your scared, scared of dying alone")
        print_pause("Tears start dropping from your eyes")
        print_pause("You start remenescing..")
        print_pause("you wait...")
        print_pause("and wait...")
        print_pause("and wait..")
        print_pause("To be continued..")


def inclosed_room_second_choice(): #Second room choice basically
    global player_attributes #Where you can fight and do other things

    print_pause("You hear a weird noise")
    print_pause("A man enters the room")
    print_pause("He is MASKED")
    print_pause("The masked tries to attack")
    print_pause("You try to dodge")

    if player_attributes["Thirsty"]:
        print_pause("You are too dehydrated, the masked man slashes you...")
        print_pause("You died...")
        return
    else:
        print_pause("You were able to dodge")
        print_pause("Nice dodge")
        increase_score(20)
        Choice = check_choice("[1] Shout, [2] Run away, [3] Fight"
                              ,["1", "2", "3"])
        if Choice == "1":

            print_pause("The masked feels DIZZY")
            print_pause("You were able to exit the room and run past him")
            increase_score(20)
            print_pause("You continue running till you reach another exit")
            print_pause("You managed to escape but where are you?")
            print_pause("To be continued")
            return
        elif Choice == "2":
            print_pause("The masked is able to slash you...")
            print_pause("You died...")
            return
        elif Choice == "3":
            return True


def inclosed_room_third_choice(): #Room third choice
    #Nothing much just doing some storytelling
    print_pause("You continue to sleep for a while...")
    print_pause("You were slashed while sleeping..")
    print_pause("You died...")
    return

#Main game function
def game():
    global player_attributes

    print_pause("MASKED \n __________________")
    check_choice("Press any button to start", "any")

    print_pause("You feel thirsty...")
    print_pause("There is a water bottle next to you")
    Choice = check_choice("Drink from the bottle? Press 1 to drink or 2 not to"
                          , ["1", "2"], number_fail)

    #Water botlle gameplay plus introducing randomisation mechanic
    if Choice == "1":
        #Using randomization to add more custom gameplay
        Die = random.randint(1,3) == 3
        if Die:
            print_pause("You have been poisoned!")
            print_pause("You died..")
            return
        else:
            player_attributes["Thirsty"] = False
            print_pause("You feel refreshed")
            print_pause("Good for you!")
            increase_score(10)
    else:
        print("You still feel thirsty")
        player_attributes["Thirsty"] = True

    print_pause("""It looks like your in an inclosed
 room with large metal walls""")
    print_pause("What do you do?")

    #Inclosed room gameplay
    Choice = check_choice("""
[1] check the door of the room,
[2] stay on your bed,
[3] sleep?""", ["1", "2", "3"], "Choose 1 or 2 or 3")

    if Choice == "1":
        inclose_room_first_choice()
        return
    elif Choice == "2":
        Fight = inclosed_room_second_choice()
        if Fight == True:
            battle()
            return
    else:
        inclosed_room_third_choice()


while True:
    game()
    print("You final score is ", player_attributes["Score"])
    Choice = check_choice("Do you want to play again Y/N "
                          ,["Y", "N", "y", "n"], character_fail)

    if Choice.capitalize() == "N":
        break

    player_attributes["Score"] = 0
    player_attributes["Thirsty"] = True
