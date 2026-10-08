
import time
Game_loop = True

Level = 1

#Small figure variables
Strange_figure_hit= 2
Strange_figure_hit_choice = "basic hit"
Strange_figure_health = 20


#Player Variables
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
    global player_health, Strange_figure_health, scared,strange_figure_hit, Player_hit

    print("The fIguRe sTarts tO cOnsUme yOur mind...")
    print("(𓁹𓂏𓁹)")
    print("")
    if scared:
        print("The figure attacks you, you feel dizzy and your vision blurs...")
        player_health = max(0, player_health - Strange_figure_hit)
        print("Your health is now:", player_health)
        print("Your turn to attack...")
        print("Choose your attack: (basic hit), (special hit), (ultimate hit),(dodge),(heal)")
        player_hit_choice = input("Enter your choice: ")
        if player_hit_choice.lower() == "basic hit":
            print("player does a basic hit!")
            Strange_figure_health = max(0, Strange_figure_health - Player_hit)
        elif player_hit_choice.lower() == "special hit":
            print("player does a special hit!")
            Strange_figure_health = max(0, Strange_figure_health - (Player_hit * 2))
        elif player_hit_choice.lower() == "ultimate hit":
            print("player does an ultimate hit!")
            Strange_figure_health = max(0, Strange_figure_health - (Player_hit * 3))
        else:
            print("You missed!")
        print("")

        if player_health == 0:
            print("You fall before the strange figure...")
            return False
        if Strange_figure_health == 0:
            print("You defeated the small strange figure!")
            return True
    else:
        print("The figure attacks you, but you manage to dodge it...")
        Strange_figure_health = max(0, Strange_figure_health - Player_hit)
        print("The figure's health is now:", Strange_figure_health)
        print("")

    return player_health > 0


def level1():
    Strange_figure_hit= 2
    Strange_figure_hit_choice = "basic hit"
    Strange_figure_health = 20
    #Player Variables
    scared = False
    player_health = 20
    Player_hit = 2
    Player_hit_choice = "basic hit"
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
                print("You are scared", name)
                scared = True

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
        strange_figure_fight()
        time.sleep(1)
    else:
        choice = input("Invalid choice. Please choose 'left' or 'right': ")
    return scared, Strange_figure_hit



while Game_loop:
    name = start_game_settings()
    scared, Strange_figure_hit = level1()
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
