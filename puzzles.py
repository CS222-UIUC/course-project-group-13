from backend_rs import clue_one_password
from backend_rs import clue_two_password
from backend_rs import clue_three_password
from backend_rs import get_key_one_for_inventory
from backend_rs import year_puzzle_one

"""includes the implementations of the puzzles"""

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
