"""includes a few functions to determine whether players solved puzzles correctly"""
PASSWORD1 = "vector"
PASSWORD2 = "runtime"
#
level = 1 #indicates the current number of the game's level
points = 0 #the number of points the player has
increase = 3 #how many more points can be gained when a question is answered correctly
keyone = 0 #checks if a player has obtained a key or prize from the inventory

def clue_one_password(password):
    """check if player solves clue one correctly"""
    global increase
    global points
    if password == PASSWORD1:
        points = points + increase
        print("Correct! You earned " + str(increase) + " points for a total of " + str(points))
    else:
        increase = increase - 1
        if increase > 0:
            print("Incorrect. You have " + str(increase) + " tries remaining.")
        else:
            print("This puzzle is now unavailable")

def clue_two_password(password):
    """check if player solves clue two correctly"""
    global increase
    global points
    if password == PASSWORD2:
        points = points + increase
        print("Correct! You earned " + str(increase) + " points for a total of " + str(points))
    else:
        increase = increase - 1
        if increase > 0:
            print("Incorrect. You have " + str(increase) + " tries remaining.")
        else:
            print("This puzzle is now unavailable")

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

# def test_cases_function(helper):
#     print("Ignore the first test")
#     print(helper == "")
#     print("Testing if points increase if correct answer is given")
#     clue_one_password("vector")
#     print(points == 3)
#     print("Testing if points increase if correct answer is given")
#     clue_two_password("runtime")
#     print(points == 6)
#     print("Testing if attempts decrease if wrong answer is given")
#     clue_one_password("runtime")
#     print(increase == 2)
#     print("Testing if attempts decrease if wrong answer is given")
#     clue_two_password("vector")
#     print(increase == 1)
#     print("Testing if level increases when points reach threshold")
#     oldlevel = level
#     oldpoints = points
#     get_key_one_for_inventory()
#     print(level > oldlevel)
#     print("Testing if points decrease when prize is obtained")
#     print(points < oldpoints)
#     print("Testing if prize is obtained in variable")
#     print(keyone == 1)
