"""includes a few functions to determine whether players solved puzzles correctly"""
from ast import Num


PASSWORD1 = "vector"
PASSWORD2 = "This project deserves an A!"
PASSWORD3 = "binary"
YEAR = 1996

level = 1 #indicates the current number of the game's level
points = 0 #the number of points the player has
increase = 3 #how many more points can be gained when a question is answered correctly
keyone = 0 #checks if a player has obtained a key or prize from the inventory
keytwo = 0
keythree = 0
completed = 0

def level_changer():
    """allows player to continue to the next stage based on items in inventory"""
    global level
    global keyone
    global keytwo
    global keythree
    global completed
    if level == 1:
        if keyone == 1:
            level = 2
            return 2
        else:
            return 1
    elif level == 2:
        if keytwo == 1:
            level = 3
            return 3
        else:
            return 2
    elif level == 3:
        if keythree == 1:
            completed = 1
            print("Congratulations! You finished the escape room")
            return 4
        else:
            return 3

def clue_one_password(password):
    """check if player solves clue one correctly"""
    global increase
    global points
    if password == PASSWORD1:
        points = points + increase
        print("Correct! You earned " + str(increase) + " points for a total of " + str(points))
        return 1 #to indicate to the puzzle that it is solved
    else:
        increase = increase - 1
        if increase > 0:
            print("Incorrect. You have " + str(increase) + " tries remaining.")
            return 0 #to indicate to the puzzle that it is unsolved
        else:
            print("This puzzle is now unavailable")
            return -1 #to indicate that the puzzle is unavailable

def clue_two_password(password):
    """check if player solves clue two correctly"""
    global increase
    global points
    if password == PASSWORD2:
        points = points + increase
        print("Correct! You earned " + str(increase) + " points for a total of " + str(points))
        return 1
    else:
        increase = increase - 1
        if increase > 0:
            print("Incorrect. You have " + str(increase) + " tries remaining.")
            return 0
        else:
            print("This puzzle is now unavailable")
            return -1

def clue_three_password(password):
    """check if player identifies image from stage 1 correctly"""
    global increase
    global points
    if password == PASSWORD3:
        points = points + increase
        print("Correct! You earned " + str(increase) + " points for a total of " + str(points))
        return 1
    else:
        increase = increase - 1
        if increase > 0:
            print("Incorrect. You have " + str(increase) + " tries remaining.")
            return 0
        else:
            print("This puzzle is now unavailable")
            return -1

def year_puzzle_one(integer_input):
    """check if player sorts number clues correctly"""
    global points
    global level
    if integer_input % 10000 >= 1:
        print("Your input is too large")
    elif integer_input % 1000 == 0:
        print("Your input is too small")
    else:
        if integer_input == YEAR:
            points = points + increase
            print("Correct! You earned " + str(increase) + " points for a total of " + str(points))
            return 1
        else: 
            increase = increase - 1
            if increase > 0:
                print("Incorrect. You have " + str(increase) + " tries remaining.")
                return 0
            else:
                print("This puzzle is now unavailable")
                return -1

def get_key_one_for_inventory():
    """player adds a new key to the inventory"""
    global points
    global level
    global keyone
    required = 3
    if points < required:
        print("You need "+str(required-points)+" more points. Continue solving puzzles")
    else:
        print("Description: this key unlocks the next level.")
        level = level + 1
        keyone = 1
        points = points - required

def print_points() -> int:
    """getter for points"""
    return points

def print_increase() -> int:
    """getter for increase"""
    return increase

def print_level() -> int:
    """getter for level"""
    return level

def print_keyone() -> int:
    """getter for status of having prize"""
    return keyone

"""setters for global variables (mostly for testing purposes)"""
def set_points(n):
    global points
    points = n

def set_increase(n):
    global increase
    increase = n

def set_level(n):
    global level
    level = n

def set_keyone(n):
    global keyone
    keyone = n

