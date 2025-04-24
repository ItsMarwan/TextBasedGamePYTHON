# MADE BY MARWAN - 24/04/2025
# Import Modules
import time
import random

# Define important game variables
has_wand = False
has_scroll = False
points = 0
points_decrease = 0
colors = [
    "Red",
    "Pink",
    "Purple",
    "Blue",
    "Green",
    "Yellow",
    "Orange",
    "White",
    "Violet",
]
monster_list = [
    "Evil Fairy",
    "Pirate",
    "Goblin",
    "Wizard",
    "Troll",
    "Ghost",
    "Demon",
    "Vampire",
]
monster = "None"
game_over = False


# Main game functions

# The Most Used Function In This Project
def print_pause(message, delay):
    print(message)
    time.sleep(delay)


# House Choices
def house_choice():
    global game_over
    print_pause("You approach the door of the house.", 2)
    print_pause(
        f"You are about to knock when the door opens and out steps a "
        f"{monster}!",
        2,
    )
    print_pause(f"Eep! This is the {monster}'s house!", 2)

    while not game_over:
        if not has_wand:
            print_pause(
                "You feel a bit under-prepared for this, what with only "
                "having a tiny, rusty old magic wand.",
                2,
            )
        else:
            print_pause(f"The {monster} finds you!", 2)
        print_pause(
            f"Would you like to (1) cast a spell or (2) run away? "
            f"(Total Points: {points})",
            1,
        )
        choice = input(f"(Please enter 1 or 2.) (Total Points: {points})")
        if choice == "1":
            if not has_wand:
                defend_yourself(1)
            else:
                defend_yourself(2)
            break
        elif choice == "2":
            field_choice()
            break
        else:
            print_pause("====Please ONLY enter 1 or 2====", 1)
        if game_over:
            break


# Conditions For Actions Of Defending Yourself
def defend_yourself(scene):
    global points
    global points_decrease
    global game_over
    if scene == 1:
        points_decrease = random.randint(1, 10)
        points -= points_decrease
        print_pause("You do your best...", 2)
        print_pause(
            f"But your rusty old magic wand is no match for {monster}! "
            f"(-{points_decrease} Points)",
            2,
        )
        restart_game("lose")
    elif scene == 2:
        points_decrease = random.randint(1, 10)
        points += points_decrease
        print_pause(
            f"As the {monster} moves to cast a spell, you raise your new "
            f"Wand of Ogoroth. (+{points_decrease} Points)",
            2,
        )
        print_pause(
            "The Wand of Ogoroth shines brightly in your hand as you brace "
            "yourself for the spell.",
            2,
        )
        print_pause(
            f"But the {monster} takes one look at your shiny new wand and "
            f"runs away!",
            2,
        )
        print_pause(
            f"You have rid the town of the {monster}. You are victorious!",
            2,
        )
        restart_game("win")


# Makes The Player Go To The Field
def field_choice():
    global points
    global points_decrease
    print_pause("You run back into the field.", 1)
    points_decrease = random.randint(1, 10)
    points -= points_decrease
    print_pause(
        f"Luckily, you don't seem to have been followed "
        f"(-{points_decrease} Points) (Total Points: {points})",
        2,
    )
    check_choice()


# Restarts The Game
def restart_game(outcome):
    global points
    global points_decrease
    global has_wand
    global game_over
    if outcome == "lose":  # losing the game
        print(f"========================= LOSE (Total Points: {points}) ==")
        print_pause("Would you like to play again? (y/n)", 2)
    elif outcome == "win":  # winning the game
        print(f"========================= WIN (Total Points: {points}) ==")
        print_pause("Would you like to play again? (y/n)", 2)
    elif outcome == "secret":  # the secret ending
        print(f"========================= SECRET (Total Points: {points}) ==")
        print_pause("Would you like to play again? (y/n)", 2)

    while True:
        play_again = input("(Please enter Y or N.)").lower()
        if play_again == "y":
            has_wand = False
            points = 0
            points_decrease = 0
            game_over = False
            play_game()
            break
        elif play_again == "n":
            print("Game Stopped!")
            game_over = True
            break
        else:
            print_pause("Invalid input. Please enter Y or N.", 2)


# Main decision-making loop
def check_choice():
    global has_scroll
    global has_wand
    global points
    global game_over
    while not game_over:
        if points <= -10:
            restart_game("lose")
            break
        print_pause(f"What would you like to do? (Total Points: {points})", 1)
        print_pause("Enter 1 to knock on the door of the house.", 1)
        print_pause("Enter 2 to peer into the cave.", 1)
        if has_scroll:
            print_pause("Enter 3 to Turn Into a Monster.", 1)
            choice = input("(Please enter 1 or 2 or 3.)")
            if choice == "1":
                house_choice()
                break
            elif choice == "2":
                cave_choice()
                break
            elif choice == "3":
                be_monster()
                break
            else:
                print_pause("====Please ONLY enter 1 or 2 or 3====", 1)
        else:
            choice = input("(Please enter 1 or 2.)")
            if choice == "1":
                house_choice()
                break
            elif choice == "2":
                cave_choice()
                break
            else:
                print_pause("====Please ONLY enter 1 or 2====", 1)


# Enter The Cave Choice
def cave_choice():
    scroll_chance = random.randint(1, 100)
    print_pause("You peer cautiously into the cave.", 2)
    print_pause("It turns out to be only a very small cave.", 2)
    global has_wand
    global has_scroll
    global points
    global points_decrease
    if not has_wand:
        points_decrease = random.randint(1, 10)
        points += points_decrease
        has_wand = True
        print_pause("Your eye catches a glint of metal behind a rock.", 2)
        print_pause(
            f"You have found the {random.choice(colors)} magical Wand of "
            f"Ogoroth! (+{points_decrease} Points) (Total Points: {points})",
            2,
        )
        print_pause(
            "You discard your rusty old magic wand and take the Wand of "
            "Ogoroth with you.",
            2,
        )
        print_pause("You walk back out to the field.", 2)
        check_choice()
    else:
        if scroll_chance == random.randint(1, 100):
            has_scroll = True
            print_pause("You Look Around And By Chance You Find a Scroll", 2)
            print_pause("You Now Can Become The Monster!", 2)
            print_pause("You Walk Back Out To The Field.", 2)
            check_choice()
        else:
            print_pause("You Look Around But You Dont Find Anything.", 2)
            print_pause("You Walk Back Out To The Field.", 2)
            check_choice()


# "become the monster" secret ending
def be_monster():
    global points
    global game_over
    print_pause(f"You Read The Scroll Out loud. (-{points} Points)", 2)
    print_pause("You Transformed Into a Monster", 2)
    print_pause(f"More Scarier Than {monster}.", 2)
    print_pause(
        f"You have rid the town of the {monster}. You are Now The New "
        f"Monster! (Total Points: {points})",
        2,
    )
    restart_game("secret")


# Starts the game
def play_game():
    global monster
    global game_over
    game_over = False
    monster = random.choice(monster_list)
    print_pause(
        f"You find yourself standing in an open field, filled with grass, "
        f"and {random.choice(colors)} wildflowers.",
        2,
    )
    print_pause(
        f"Rumor has it that a {monster} is somewhere around here, and has "
        f"been terrifying the nearby village.",
        2,
    )
    print_pause("In front of you is a house.", 2)
    print_pause("To your right is a dark cave.", 2)
    print_pause(
        f"In your hand you hold your trusty (but not very effective), "
        f"magic wand.",
        2,
    )
    check_choice()


# Start the gameplay
play_game()
