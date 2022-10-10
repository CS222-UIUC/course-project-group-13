"""includes a few functions to determine whether players solved puzzles correctly"""
from ast import Num


PASSWORD1 = "vector"
PASSWORD2 = "This project deserves an A!"
PASSWORD3 = "binary"
YEAR = 1998
DIRECTIONS = "DRDLDLDRD"

level = 1  # indicates the current number of the game's level
points = 0  # the number of points the player has
increase = 3  # how many more points can be gained when a question is answered correctly
keyone = 0  # checks if a player has obtained a key or prize from the inventory
keytwo = 0
keythree = 0
completed = 0
matchlist = (['Z', 'Z', 'Z', 'Z', 'Z'])
index = 0
credentials = ([["testusername", "testpassword", "testscore"]])


def create_account_backup(username, password):
    """backup function for creating new profile"""
    global credentials
    credentials.append([username, password, str(0)])
    
    
def sign_in_backup(username, password):
    """backup function for signing in"""
    for i in range(len(credentials)):
        if credentials[i][0] == username:
            if credentials[i][1] == password:
                print("Sign in successful")
                print("Your score is " + credentials[i][2])
                return 1
    print("Incorrect username or password")
    return 0
    

def level_changer():
    """allows player to continue to the next stage based on items in inventory"""
    global level
    global keyone
    global keytwo
    global keythree
    global points
    global completed
    global increase
    level = level + 1
    points = 0
    increase = 5
    if level == 3:
        if keythree == 1:
            print("Congratulations! You are able to move on to the next room.")
    return level


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
    global increase
    if integer_input / 1000 == 0:
        print("Your input is too small")
        return 2
    elif integer_input / 1000 >= 2:
        print("Your input is too large")
        return 2
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
        keyone = 1
        points = points - required
        level_changer()
        
        
# this puzzle below is used to solve a maze. Player types in directions of the maze
def directional_lock(directions_input):
    """checks if player correctly has solved the maze"""
    global points
    global increase
    global DIRECTIONS
    print("9 character directional code: up=U, down=D, left=L, right=R")
    if directions_input == DIRECTIONS:
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


def matching_display():
    print("Match the following terms on the right side with the clues on the left side:")
    print("1. Rotation                                   A. DFS")
    print("2. Stack                                      B. * or &")
    print("3. Segmentation-fault-causer               C. Valgrind")
    print("4. Allows for change                         D. AVL")
    print("5. Memory                                   E. NULL")


def create_match(letter):
    global matchlist
    global index
    if (index < 5):
        matchlist[index] = letter
        index = index + 1

def reset_matchlist():
    global matchlist
    global index
    index = 0
    create_match('Z')
    create_match('Z')
    create_match('Z')
    create_match('Z')
    create_match('Z')
    index = 0

def check_match():
    global matchlist
    global points
    global increase
    wrong = 0
    correctmatch = (['D', 'A', 'E', 'B', 'C'])
    for i in range(len(matchlist)):
        if matchlist[i] != correctmatch[i]:
            print("The " + str(i+1) +" entry is wrong")
            reset_matchlist()
            wrong = wrong + 1
            return 0
    if (wrong == 0):
        print("Correct! You earned " + str(increase) + " points for a total of " + str(points))
        points = points + increase
    return 1

        
def print_points() -> int:
    """getter for points"""
    return points


def print_matchlist() -> list[str]:
    """getter for matchlist"""
    return matchlist


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
