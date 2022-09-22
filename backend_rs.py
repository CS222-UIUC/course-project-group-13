PASSWORD1 = "vector"
PASSWORD2 = "runtime"
level = 1 #indicates the current number of the game's level
points = 0 #the number of points the player has
increase = 3 #how many more points can be gained when a question is answered correctly
keyone = 0 #checks if a player has obtained a key or prize from the inventory


def clue_one_password(password): #check if player solves clue one correctly
    global increase
    global points
    if password == PASSWORD1:
        print("Correct! You earned " + increase + " points.")
        points = points + increase
    else:
        increase = increase - 1
        if (increase > 0):
            print("Incorrect. You have " + increase + " tries remaining.")
        else:
            print("This puzzle is now unavailable")

def clue_two_password(password): #check if player solves clue two correctly
    global increase
    global points
    if password == PASSWORD2:
        print("Correct! You earned " + increase + " points.")
        points = points + increase
    else:
        increase = increase - 1
        if increase > 0:
            print("Incorrect. You have " + increase + " tries remaining.")
        else:
            print("This puzzle is now unavailable")

def get_key_one_for_inventory(): #player adds a new key to the inventory
    global points
    global level
    required = 3
    if points < required:
        print("Not enough points available. Continue solving puzzles")
    else:
        print("Description: this key unlocks the next level.")
        level = level + 1
        haskeyone = 1
        points = points - required
