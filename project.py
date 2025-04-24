# MADE BY MARWAN - 24/04/2025
# Import Time
import time
import random

# Important Variables
hasWand = False
hasScroll = False
Points = 0
PointsDECREASE = 0
colors = ["Red", "Pink", "Purple", "Blue", "Green", "Yellow", "Orange", "White", "Violet"]
monsterLIST = ["Evil Fairy", "Pirate", "Goblin", "Wiazrd", "Troll" , "Ghost", "Demon", "Vampire"]
monster = "None"
game_over = False

# Main Definitions

# The Most Used Definition In This Project!
def print_pause(string, Time):
    print(string)
    time.sleep(Time)

# The House Decision Outputs
def house():
    global game_over
    print_pause("You Approach The Door Of The House", 2)
    print_pause(f"You Are About To knock When The Door Opens And Out Steps a {monster}", 2)
    print_pause(f"Eep! This Is The {monster}'s House!", 2)

    while not game_over:
        if hasWand == False:
            print_pause("You Feel a Bit Under-Prepared For This, What With Only Having a Tiny, Rusty old magic wand.", 2)
        elif hasWand == True:
            print_pause(f"The {monster} finds you!", 2)
        print_pause("Would You Like to (1) cast a spell or (2) run away?", 1)
        choice1 = input("(Please enter 1 or 2.)")
        if choice1 == "1":
            if hasWand == False:
                defend(1)
            elif hasWand == True:
                defend(2)
            break
        elif choice1 == "2":
            field()
            break
        else:
            print_pause("====Please ONLY enter 1 or 2====", 1)
        if game_over:
            break

# The Defend Scene, Which Is Important Too
def defend(SCENE):
    global Points
    global PointsDECREASE
    global game_over
    if SCENE == 1:
        PointsDECREASE = random.randint(1, 10)
        Points -= PointsDECREASE
        print_pause("You Do Your Best...", 2)
        print_pause(f"But Your Rusty Old Magic Wand Is No Match For {monster}!  (-{PointsDECREASE} Points)", 2)
        restart("lose")
    elif SCENE == 2:
        PointsDECREASE = random.randint(1, 10)
        Points += PointsDECREASE
        print_pause(f"As the {monster} moves to cast a spell, you raise your new Wand of Ogoroth.  (+{PointsDECREASE} Points)", 2)
        print_pause("The Wand of Ogoroth shines brightly in your hand as you brace yourself for the spell.", 2)
        print_pause(f"But the {monster} takes one look at your shiny new wand and runs away!", 2)
        print_pause(f"You have rid the town of the {monster}. You are victorious!", 2)
        restart("win")

# Running Back To The Field Choice
def field():
    global Points
    global PointsDECREASE
    print_pause("You Run Back into the field.", 1)
    PointsDECREASE = random.randint(1, 10)
    Points -= PointsDECREASE
    print_pause(f"Luckily, you don't seem to have been followed (-{PointsDECREASE} Points)", 2)
    loop()

# Restart Definition, Used For Replayability
def restart(TYPE):
    global Points
    global PointsDECREASE
    global hasWand
    global game_over
    if TYPE == "lose": # The Screen When The PLayer Loses The Game

        print("========================= LOSE =========================")
        print_pause("Would you like to play again? (y/n)", 2)

        hasWand = False
        Points = 0
        PointsDECREASE = 0
        while True:
            choice1 = input("(Please enter Y or N.)").lower()
            if choice1 == "y":
                game_over = False
                play()
                break
            elif choice1 == "n":
                print("Game Stopped!")
                game_over = True
                break
            else:
                print_pause("Invalid input. Please enter Y or N.", 2)
    elif TYPE == "win": # The Screen When The Player Wins The Game

        print("========================= WIN =========================")
        print_pause("Would you like to play again? (y/n)", 2)

        hasWand = False
        Points = 0
        PointsDECREASE = 0
        while True:
            choice1 = input("(Please enter Y or N.)").lower()
            if choice1 == "y":
                game_over = False
                play()
                break
            elif choice1 == "n":
                print("Game Stopped!")
                game_over = True
                break
            else:
                print_pause("====Please ONLY enter Y or N====", 1)
    elif TYPE == "secret": # The Screen When The Player Uses The Secret Of The Game

        print("========================= SECRET =========================")
        print_pause("Would you like to play again? (y/n)", 2)

        hasWand = False
        Points = 0
        PointsDECREASE = 0
        while True:
            choice1 = input("(Please enter Y or N.)").lower()
            if choice1 == "y":
                game_over = False
                play()
                break
            elif choice1 == "n":
                print("Game Stopped!")
                game_over = True
                break
            else:
                print_pause("====Please ONLY enter Y or N====", 1)

# Decision Making Loop (MOST IMPORTANT DEFINITION)
def loop():
    global hasScroll
    global hasWand
    global Points
    global game_over
    while not game_over:
        if Points <= -10:
            restart("lose")
            break
        print_pause("What would you like to do?", 1)
        print_pause("Enter 1 to knock on the door of the house.", 1)
        print_pause("Enter 2 to peer into the cave.", 1)
        if hasScroll == True:
            print_pause("Enter 3 to Turn Into a Monster.", 1)
            choice1 = input("(Please enter 1 or 2 or 3.)")
            if choice1 == "1":
                house()
                break
            elif choice1 == "2":
                cave()
                break
            elif choice1 == "3":
                Bemonster()
                break
            else:
                print_pause("====Please ONLY enter 1 or 2 or 3====", 1)
        else:
            choice1 = input("(Please enter 1 or 2.)")
            if choice1 == "1":
                house()
                break
            elif choice1 == "2":
                cave()
                break
            else:
                print_pause("====Please ONLY enter 1 or 2====", 1)

# Cave Decision
def cave():
    scrollChance = random.randint(1, 100)
    print_pause("You peer cautiously into the cave.", 2)
    print_pause("It turns out to be only a very small cave.", 2)
    global hasWand
    global hasScroll
    if hasWand == False:
        hasWand = True
        print_pause("Your eye catches a glint of metal behind a rock.", 2)
        print_pause(f"You have found the {random.choice(colors)} magical Wand of Ogoroth!", 2)
        print_pause("You discard your rusty old magic wand and take the Wand of Ogoroth with you.", 2)
        print_pause("You walk back out to the field.", 2)
        loop()
    else:
        if scrollChance == random.randint(1, 100):
            hasScroll = True
            print_pause("You Look Around And By Chance You Find a Lost Scroll", 2)
            print_pause("You Now Can Become The Monster!", 2)
            print_pause("You Walk Back Out To The Field.", 2)
            loop()
        else: 
            print_pause("You Look Around But You Dont Find Anything.", 2)
            print_pause("You Walk Back Out To The Field.", 2)
            loop()

# Secret Ending of The Game
def Bemonster():
    global Points
    global game_over
    print_pause(f"You Read The Scroll Out loud.  (-{Points} Points)", 2)
    print_pause("You Transformed Into a Monster", 2)
    print_pause(f"More Scarier Than {monster}.", 2)
    print_pause(f"You have rid the town of the {monster}. You are Now The New Monster!", 2)
    restart("secret")

# Starts The Game
def play():
    global monster
    global game_over
    game_over = False
    monster = random.choice(monsterLIST)
    print_pause(f"You find yourself standing in an open field, filled with grass, and {random.choice(colors)} wildflowers.", 2)
    print_pause(f"Rumor has it that a {monster} is somewhere around here, and has been terrifying the nearby village.", 2)
    print_pause("In front of you is a house.", 2)
    print_pause("To your right is a dark cave.", 2)
    print_pause("In your hand you hold your trusty (but not very effective), magic wand.", 2)
    loop()

# Main Start Gameplay, Which Is Just One Line Of Code!
play()