from backend_rs import clue_one_password
from backend_rs import clue_two_password
from backend_rs import clue_three_password
from backend_rs import get_key_one_for_inventory
from backend_rs import year_puzzle_one
from backend_rs import print_level

"""includes the implementations of the puzzles"""

def puzzle_chooser():
    """allows player to choose a puzzle they would like to attempt (this will change once we start the front end)"""
    level = print_level()

    if (level == 1):
        choice = 0
        print("You are in Room 1 of the escape room. You look around and see two tables, each with an old computer. What would you like to do?")
        print("1: Look at the computer on the left")
        print("2: Look at the computer on the right")
        while True:
            choice = int(input("Enter either 1 or 2: "))
            if choice == 1 or choice == 2:
                break
            else:
                print("Invalid input.")
        if choice == 1:
            print("As you walk closer to the computer on the left, you see a sticky note with a riddle on it. On the screen of the computer, there is a place to put your answer:")
            riddle()
        if choice == 2:
            print("The computer on the right has a notepad next to it with another riddle scrawled on it in messy handwriting. The screen of the computer has a place to put your answer:")
            riddle2()
        
    elif (level == 2):
        choice = 0
        print("You walk into the next room, where you see a safe with a 4-number keypad and a nonsensical message written on one of the walls in spraypaint.")
        print("What would you like to do?")
        print("1: Walk closer to the safe")
        print("2: Walk closer to the wall")
        while True:
            choice = int(input("Enter either 1 or 2: "))
            if choice == 1 or choice == 2:
                break
            else:
                print("Invalid input.")
        if choice == 1:
            print("When you walk up to the safe, you see a clue next to the keypad. ")
            year_puzzle()
        if choice == 2:
            print("You walk closer to the wall with the message on it, and none of it makes sense to you.")
            decode()

def riddle():
# using input for now but might have to change when we implement the front end
    while True:
        response = input("Whether I'm 1-Dimensional, 2-Dimensional, or 3-Dimensional, I'm still the same. You can change my size, but you can't change my type or my name. What am I? ")
        correct = clue_one_password(response)
        if correct == 1:
            get_key_one_for_inventory() #if correct, the user gets a key
            return
        elif correct == 0:
            again = input("Would you like to try again? Y/N ")
            if again == "N":
                return
        else:
            return

        
def decode():
    # uses Caesar cipher, which we could put a hint to (or a link to an online translator) as a reward for solving one of the other puzzles
    while True:
        print("Decode the following message: ")
        print()
        print("Wklv surmhfw ghvhuyhv dq D!")
        print()
        response = input("What does this code say? ")
        correct = clue_two_password(response)
        if correct == 1:
            return
        elif correct == 0:
            again = input("Would you like to try again? Y/N ")
            if again == "N":
                return
        else:
            return

def riddle2():
    while True:
        response = input("I'm used to build a computer, but you can't hold me in your hands. There's two shapes I can take: a line or a circle. What am I? ")
        correct = clue_three_password(response)
        if correct == 1:
            return
        elif correct == 0:
            again = input("Would you like to try again? Y/N ")
            if again == "N":
                return
        else:
            return

def year_puzzle():
    while True:
        response = input("In what year was Google founded?")
        correct = year_puzzle_one(int(response))
        if correct == 1:
            return
        elif correct == 0:
            again = input("Would you like to try again? Y/N ")
            if again == "N":
                return
        elif correct == -1:
            return

        
def riddle_automatic():
#  used only for testing, so has pre-set input. 
    while True:
        response = "vector"
        correct = clue_one_password(response)
        if correct == 1:
            get_key_one_for_inventory() #if correct, the user gets a key
            return
        elif correct == 0:
            again = input("Would you like to try again? Y/N ")
            if again == "N":
                return
        else:
            return

        
def decode_automatic():
    # used in test file and has pre-set input. uses Caesar cipher, which we could put a hint to (or a link to an online translator) as a reward for solving one of the other puzzles
    while True:
        print("Decode the following message: ")
        print()
        print("Wklv surmhfw ghvhuyhv dq D!")
        print()
        response = "This project deserves an A!"
        correct = clue_two_password(response)
        if correct == 1:
            return
        elif correct == 0:
            again = input("Would you like to try again? Y/N ")
            if again == "N":
                return
        else:
            return

def riddle2_automatic():
    while True:
        response = "binary"
        correct = clue_three_password(response)
        if correct == 1:
            return
        elif correct == 0:
            again = input("Would you like to try again? Y/N ")
            if again == "N":
                return
        else:
            return

def year_puzzle_automatic():
    while True:
        response = "1998"
        correct = year_puzzle_one(int(response))
        if correct == 1:
            return
        elif correct == 0:
            again = input("Would you like to try again? Y/N ")
            if again == "N":
                return
        elif correct == -1:
            return
