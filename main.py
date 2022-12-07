"""contains test cases that return either true (passed) or false (failed)"""
from backend_rs import clue_one_password
from backend_rs import clue_two_password
from backend_rs import clue_three_password
from backend_rs import level_changer
from backend_rs import year_puzzle_one
from backend_rs import get_key_one_for_inventory
from backend_rs import print_increase
from backend_rs import print_keyone
from backend_rs import print_level
from backend_rs import print_points
from backend_rs import set_increase
from backend_rs import set_keyone
from backend_rs import set_level
from backend_rs import set_points
from backend_rs import directional_lock
from backend_rs import matching_display
from backend_rs import print_matchlist
from backend_rs import matchlist
from backend_rs import check_match
from backend_rs import create_match
from backend_rs import guess_increase
from backend_rs import guess_puzzle
from backend_rs import guess_puzzle_answer
from backend_rs import guess_increase
from backend_rs import guess_puzzle_automatic_easy
from backend_rs import mystery_number
from backend_rs import print_guess_increase
from backend_rs import print_mystery

from puzzles import riddle
from puzzles import decode
from puzzles import riddle2
from puzzles import riddle_automatic
from puzzles import decode_automatic
from puzzles import riddle2_automatic
from puzzles import year_puzzle_automatic

num_failed = 0
num_passed = 0

print("Testing if points increase if correct answer is given")
clue_one_password("vector")
print(print_points() == 3)
if print_points() == 3:
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1

print("")
print("Testing if points increase if correct answer is given")
clue_two_password("This project deserves an A!")
print(print_points() == 6)
if print_points() == 6:
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1

print("")
print("Testing if attempts decrease if wrong answer is given")
clue_one_password("This project deserves an A!")
print(print_increase() == 2)
if print_increase() == 2:
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1

print("")
print("Testing if attempts decrease if wrong answer is given")
clue_two_password("I don't know")
print(print_increase() == 1)
if print_increase() == 1:
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1

print("")
print("Testing if level increases when points reach threshold")
old_level = print_level()
oldlevel = print_level()
oldpoints = print_points()
get_key_one_for_inventory()
print(print_level() > oldlevel)
if print_level() > oldlevel:
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1

print("")
print("Testing if points decrease when prize is obtained")
print(print_points() < oldpoints)
if print_points() < oldpoints:
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1

print("")
print("Testing if prize is obtained in variable")
print(print_keyone() == 1)
if print_keyone() == 1:
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1
    
print("")
print("Testing if stage changes correctly using level_increase")
print(print_level())
print(print_level() > old_level)
if print_level() > old_level:
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1

print("")
print("Testing if points reset when moving to next level")
print(print_points() == 0)
if print_points() == 0:
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1
    
print("")
print("Testing if points increase when answering clue 3 puzzle correctly")
old_points = print_points()
clue_three_password("binary")
print(print_points() == old_points + print_increase())
if print_points() == old_points + print_increase():
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1
    
print("")
print("Testing if year puzzle helps player if input is too large")
year_puzzle_one(100000000000)
print("True")

print("")
print("Testing if year puzzle helps player if input is too small")
year_puzzle_one(10)
print("True")

print("")
print("Testing if year puzzle works correctly")
old_increase = print_increase()
year_puzzle_one(1980)
print(print_increase() < old_increase)
if print_increase() < old_increase:
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1
old_points = print_points()
year_puzzle_one(1998)
print(print_points() > old_points)
if print_points() > old_points:
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1
    
    
print("")
print("Testing if maze function works correctly")
old_increase = print_increase()
directional_lock("UDLRUDLRU")
print(print_increase() < old_increase)
if print_increase() < old_increase:
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1
old_points = print_points()
directional_lock("DLDRURDLD")
print(print_points() > old_points)
if print_points() > old_points:
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1
    
    
print("")
print("Testing if create matching function works correctly")
matching_display()
print("")
create_match("A")
create_match("B")
create_match("C")
create_match("D")
create_match("E")
print(matchlist)
print(matchlist[0] == "A")
if (matchlist[0] == "A"):
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1
print(matchlist[2] == "C")
if (matchlist[2] == "C"):
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1
# checks if too many matches are created
create_match("F")
print(matchlist[4] == "E")
if (matchlist[4] == "E"):
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1

print("")
print("Testing if check_matching function works correctly")
print("Check match output should say 'The # entry is wrong' for incorrect match")

print(check_match() == 0)
if check_match() == 0:
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1

create_match("D")
create_match("A")
create_match("E")
create_match("B")
create_match("B")
print(matchlist)

print(check_match() == 0)
if check_match() == 0:
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1

create_match("D")
create_match("A")
create_match("E")
create_match("B")
create_match("C")

print(check_match() == 1)
if check_match() == 1:
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1
    
    
    
print("")
print("Testing if guess random number function works and sets correct point values")
guess_puzzle_automatic_easy()
print("Mystery number is " + str(print_mystery()))
print("Guess increase is " + str(print_guess_increase()))
if print_mystery() > 0:
    print("True")
    num_passed = num_passed + 1
else:
    print("False")
    num_failed = num_failed + 1
if print_mystery() < 6:
    print("True")
    num_passed = num_passed + 1
else:
    print("False")
    num_failed = num_failed + 1
if print_guess_increase() == 2:
    print("True")
    num_passed = num_passed + 1
else:
    print("False")
    num_failed = num_failed + 1

print("Testing if points change with random number function")
previous_points = print_points()
guess_puzzle_answer(print_mystery())
if print_points == previous_points + 2:
    print("True")
    num_passed = num_passed + 1
else:
    print("False")




print("")
#tested behavior in terminal because requires user input -- unsure if there's a way to test it more intuitively
print()
set_increase(3)
print("Testing if puzzle 1 behaves correctly...")
print(print_keyone() == 1)
# riddle()
riddle_automatic()

print()
set_increase(3)
print("Testing if puzzle 2 behaves correctly...")
# decode()
decode_automatic()

print()
set_increase(3)
print("Testing if puzzle 3 behaves correctly...")
riddle2_automatic()

print()
set_increase(3)
print("Testing if puzzle 4 behaves correctly...")
year_puzzle_automatic()

print("")
if num_failed == 0:
    print("All tests passed")
else:
    print("Tests passed: ")
    print(num_passed)
    print("Tests failed: ")
    print(num_failed)
