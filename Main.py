
import time
Game_loop = True

Level = 1
player_health = 20
Strange_figure_hit= 2
Strange_figure_hit_choice = "basic hit"

scared = ""

Player_hit = 2
Player_hit_choice = "basic hit"

name = ""

def start_game_settings():
    print("---------------Welcome------------------")
    print("What's Your Name?")
    name = input("Enter name: ")
    return name

def loading():
    print("loading.")
    time.sleep(0.5)
    print("loading..")
    time.sleep(0.5)
    print("loading...")
    time.sleep(0.5)

def strange_figure_fight():
    print("The fIguRe sTarts tO cOnsUme yOur mind...")
    if scared:
        print("The figure attacks you, you feel dizzy and your vision blurs...")
        player_health -= Strange_figure_hit
        print("Your health is now:", player_health)
        print("")

    


def level1():
    level = 1
    loading()

    print("(𓁹𓂏𓁹) hello", name)
    print("Level 1: The Beginning")
    print("Infront of you are two doors, the one on the left is a bright color red and the one on the right is blue")
    print("Which door do you choose? (left/right)")
    print("")
    choice = input("Enter your choice: ")
    if choice.lower() == "left":

        print("You enter the left door...")
        print("behind you there is a weird small figure, it has a big head with a small body. His eyes look at you with awe")
        print("Do you want to get closer to the figure? (yes/no)")
        choice2 = input("Enter your choice: ")


        if choice2.lower() == "yes":
            print("You approach the figure...")
            print("What a... Stranger person you are", name)
            print("Aren't you scared?")

            scared = input("Are you scared? (yes/no): ")
            if scared.lower() == "yes":
                print("You are scared", name)
            elif scared.lower() == "no":
                print("You are brave", name)
                print("Or are you just ignorant? ")


        elif choice2.lower() == "no":
            print("You decide to stay back...")
            print("While you walk away from the figure, it disapears from your sight.")
        else:
            choice2 = "no"

    elif choice.lower() == "right":
        print("You enter the right door...")
        print("There is nothing more strange than someone hiding ")
    else:
        choice = input("Invalid choice. Please choose 'left' or 'right': ")
        level1()  
    return scared





while Game_loop:

    name = start_game_settings()
    scared = level1()
    level1()
    print("Level 1 completed!")
    print("Scared level:", scared)
    print("Strange figure hit:", Strange_figure_hit)


    print("Do you want to continue to restart? (yes/no)")
    choice = input("Enter your choice: ")
    if choice.lower() == "no":
        Game_loop = False
        print("Thanks for playing!")
    else:
        print("Restarting the game...")
        time.sleep(1)
        print("Game has restarted")
