import time
import random
import pycodestyle

fchecker = pycodestyle.Checker('main.py', show_source=True)
file_errors = fchecker.check_all()

print("Found %s errors (and warnings)" % file_errors)


GAME_IS_ON = True
objects = ["Rock", "Sword", "Peanut butter and jelly sandwich"]


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f"The option {option} is invalid. Try again")


def play_again():
    play_again = valid_input("Enter 1 to play again or 2 to exit.", ["1", "2"])
    if play_again == "1":
        GAME_IS_ON = True
        play_game()
    elif play_again == "2":
        print("Goodbye")
        GAME_IS_ON = False


def print_pause(instructions):
    print(instructions)
    time.sleep(2)


def run_away():
    print("Keep running!! Looks like there is a safe village ahead.")
    GAME_IS_ON = False
    play_again()


def tko_shrek():
    print("Congrats! You knocked out Shrek\nRun free to the village!")
    GAME_IS_ON = False
    play_again()


def knock_door():
    print("Shrek opens the door and screams in your face!!")
    time.sleep(1)
    choice_2 = valid_input("Enter 1 to run away Or 2 to punch him", ["1", "2"])
    if choice_2 == "1":
        run_away()
    elif choice_2 == "2":
        tko_shrek()


def pick_object():
    random_object = random.choice(objects)
    print_pause(f"You picked up {random_object}")
    print("Unfortunately you still can't see\nYou fall into a hole")
    print("Game Over")


def enter_cave():
    print("It's very cold and dark here\nYou can't see where you are stepping")
    time.sleep(0.5)
    choice_3 = valid_input("Press 1knock on house or 2pick object", ["1", "2"])
    if choice_3 == "1":
        print_pause("Excellent choice.\nLet's go see who's in the house.")
        knock_door()
    elif choice_3 == "2":
        pick_object()
        GAME_IS_ON = False
        play_again()


def play_game():
    print_pause("You find yourself in an open field,\nfilled w/ flowers.")
    print_pause("Rumor has it that a wicked fairy is somewhere around here,")
    print_pause("..and has been terrifying the nearby village...")
    print("What would you do?")
    choice_1 = valid_input("Options: 1 knock on door,2 go in cave", ["1", "2"])
    if choice_1 == "1":
        knock_door()
    elif choice_1 == "2":
        enter_cave()


while GAME_IS_ON:
    play_game()
    time.sleep(2)
    break
