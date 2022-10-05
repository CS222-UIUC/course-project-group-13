from backend_rs import clue_one_password
from backend_rs import clue_two_password
from backend_rs import get_key_one_for_inventory

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
            again = "N"
            if again == "N":
                return
        else:
            return
