
#Ongoing backend development of puzzles to solve
password1 = "segfault"
password2 = "runtime"
level = 1 #indicates the current number of the game's level
points = 0 #the number of points the player has
increase = 3 #how many more points can be gained when a question is answered correctly
hasKeyOne = false #checks if a player has obtained a key or prize from the inventory

def clueOnePassword(input): #check if player solves clue one correctly
    if input == password1:
        print("Correct! You earned " + increase + " points.")
        points = points + increase
    else:
        increase = increase - 1
        if (increase > 0):
            print("Incorrect. You have " + increase + " tries remaining.")
        else:
            print("This puzzle is now unavailable")
        
        
 def clueTwoPassword(input): #check if player solves clue two correctly
    if input == password2:
        print("Correct! You earned " + increase + " points.")
        points = points + increase
    else:
        increase = increase - 1
        if (increase > 0):
            print("Incorrect. You have " + increase + " tries remaining.")
        else:
            print("This puzzle is now unavailable")
        
  def getKeyOneForInventory(): #player adds a new key to the inventory that allows for more features or a higher level
    required = 3
    if points < required:
        print("Not enough points available. Continue solving puzzles")
    else:
        print("Description: this key unlocks the next level.") 
        ++level
        points = points - required
        
        


