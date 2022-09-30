"""contains test cases that return either true (passed) or false (failed)"""
from backend_rs import clue_one_password
from backend_rs import clue_two_password
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

#tested behavior in terminal because requires user input -- unsure if there's a way to test it more intuitively
print()
set_increase(3)
print("Testing if puzzle 1 behaves correctly...")
riddle()

print()
set_increase(3)
print("Testing if puzzle 2 behaves correctly...")
decode()

print("")
if num_failed == 0:
    print("All tests passed")
else:
    print("Tests passed: ")
    print(num_passed)
    print("Tests failed: ")
    print(num_failed)
