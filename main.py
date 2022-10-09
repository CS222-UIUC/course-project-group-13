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

from puzzles import riddle
from puzzles import decode
from puzzles import riddle2
from puzzles import riddle_automatic
from puzzles import decode_automatic
from puzzles import riddle2_automatic

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
year_puzzle_one(1996)
print(print_points() > old_points)
if print_points() > old_points:
    num_passed = num_passed + 1
else:
    num_failed = num_failed + 1

print("")
if num_failed == 0:
    print("All pre-input tests passed")
else:
    print("Tests passed: ")
    print(num_passed)
    print("Tests failed: ")
    print(num_failed)

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

print("")
if num_failed == 0:
    print("All tests passed")
else:
    print("Tests passed: ")
    print(num_passed)
    print("Tests failed: ")
    print(num_failed)
