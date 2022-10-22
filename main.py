import time
import random
import pycodestyle

fchecker = pycodestyle.Checker('main.py', show_source=True)
file_errors = fchecker.check_all()

print("Found %s errors (and warnings)" % file_errors)


GAME_IS_ON = True
objects = ["Rock", "Sword", "Peanut butter and jelly sandwich"]


def play_again():
    play_again = input("Enter 1 to play again. Enter 2 to exit.")
    if play_again == "1":
        GAME_IS_ON = True
        play_game()
    elif play_again == "2":
        print("Goodbye")
        GAME_IS_ON = False
    else:
        while play_again != "1" and play_again != "2":
            try_again = input("Invalid. Please enter 1 or 2 only")
            if try_again == "1" or play_again == "1":
                play_game()
            elif try_again == "2" or play_again == "2":
                print("Goodbye")
                GAME_IS_ON = False
                break


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
    choice_2 = input("Enter 1 to run away. Enter 2 to punch him in the face")
    if choice_2 == "1":
        run_away()
    elif choice_2 == "2":
        tko_shrek()
    else:
        while choice_2 != "1" and choice_2 != "2":
            try_again = input("Invalid. Please enter 1 or 2 only")
            if try_again == "1" or choice_2 == "1":
                run_away()
            elif try_again == "2" or choice_2 == "2":
                tko_shrek()


def pick_object():
    random_object = random.choice(objects)
    print_pause(f"You picked up {random_object}")
    print("Unfortunately you still can't see\nYou fall into a hole")
    print("Game Over")


def enter_cave():
    print("It's very cold and dark here\nYou can't see where you are stepping")
    time.sleep(0.5)
    choice_3 = input("Enter 1 to go to the house\nEnter 2 to pick an object")
    if choice_3 == "1":
        print_pause("Excellent choice.\nLet's go see who's in the house.")
        knock_door()
    elif choice_3 == "2":
        pick_object()
        GAME_IS_ON = False
        play_again()
    else:
        while choice_3 != "1" and choice_3 != "2":
            try_again = input("Invalid. Please enter 1 or 2 only")
            if try_again == "1" or choice_3 == "1":
                knock_door()
            elif try_again == "2" or choice_3 == "2":
                pick_object()


def play_game():
    print_pause("You find yourself in an open field,\nfilled w/ flowers.")
    print_pause("Rumor has it that a wicked fairy is somewhere around here,")
    print_pause("..and has been terrifying the nearby village...")
    print("What would you do?")
    choice_1 = input("Enter 1 to knock on a house\nEnter 2 to go in the cave")
    if choice_1 == "1":
        knock_door()
    elif choice_1 == "2":
        enter_cave()
    else:
        while choice_1 != "1" and choice_1 != "2":
            try_again = input("Invalid. Please enter 1 or 2 only")
            if try_again == "1" or choice_1 == "1":
                knock_door()
            elif try_again == "2" or choice_1 == "2":
                enter_cave()


while GAME_IS_ON:
    play_game()
    time.sleep(2)
    break
