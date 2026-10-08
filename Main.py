
import time
Game_loop = True



Strange_figure_hit= 2
Strange_figure_hit_choice = "basic hit"
Strange_figure_health = 20


scared = False
player_health = 20
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
    while Strange_figure_health >= 0 or player_health >= 0:
        print("The fIguRe sTarts tO cOnsUme yOur mind...")
        print("(𓁹𓂏𓁹)")
        if scared == True:
            print("The figure attacks you, you feel dizzy and your vision blurs...")
            player_health -= Strange_figure_hit
        else:
            print("The figure attacks you, but you manage to dodge it...")
            Strange_figure_health -= Player_hit
    


def level1():
    level = 1
    loading()
    print("")
    print("(𓁹𓂏𓁹) hello", name)
    print("Level 1: The Beginning")
    print("Infront of you are two doors, the one on the left is a bright color red and the one on the right is blue")
    print("Which door do you choose? (left/right)")
    print("")
    choice = input("Enter your choice: ")
    if choice.lower() == "left":

        print("You enter the left door...")
        time.sleep(1)
        print("behind you there is a weird small figure, it has a big head with a small body. His eyes look at you with awe")
        print("Do you want to get closer to the figure? (yes/no)")
        choice2 = input("Enter your choice: ")
        print("")


        if choice2.lower() == "yes":
            print("You approach the figure...")
            print("-(𓁹𓂏𓁹)-")
            print("What a... Strange person you are...", name)
            print("Aren't you scared?")
            print("")
            scared = input("Are you scared? (yes/no): ")
            if scared.lower() == "yes":
                Strange_figure_hit = 10
                print("I see... you are scared", name)
                scared = True
                strange_figure_fight()
            
            elif scared.lower() == "no":
                scared = False
                print("You are brave", name)
                print("Or are you just ignorant? ")
            #Strange small figure fight
            Strange_figure_hit = 20
            time.sleep(1)






        elif choice2.lower() == "no":
            print("You decide to stay back...")
            print("While you walk away from the figure, it disapears from your sight.")
            scared = False


            
    elif choice.lower() == "right":
        time.sleep(1)
        print("You enter the right door...")
        print("When you enter the room... you see a tall figure on the corner of the room")
        scared = True
        print("The figure starts to move towards you...")
        print("He get's closer")
        #Strange tall figure fight
        time.sleep(1)
    else:
        scared = True
        choice = input("Invalid choice. Please choose 'left' or 'right': ")
    
    return scared, Strange_figure_hit



while Game_loop:
    name = start_game_settings()
    scared, Strange_figure_hit= level1()
    time.sleep(1)
    print("Level 1 completed! -------------------------------------------")
    print("")
    print("Scared? :", scared)
    print("Strange figure health:", Strange_figure_health)
    print("Strange figure hit:", Strange_figure_hit)
    print("Player health:", player_health)

    print("Do you want to continue to restart? (yes/no)")
    choice = input("Enter your choice: ")
    if choice.lower() == "no":
        Game_loop = False
        print("Thanks for playing!")
    else:
        print("Restarting the game...")
        time.sleep(1)
        print("Game has restarted")
