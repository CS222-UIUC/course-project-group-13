"""contains test cases that return either true (passed) or false (failed)"""
from backend_rs import clue_one_password
from backend_rs import clue_two_password
from backend_rs import get_key_one_for_inventory
from backend_rs import print_increase
from backend_rs import print_keyone
from backend_rs import print_level
from backend_rs import print_points

print("Testing if points increase if correct answer is given")
clue_one_password("vector")
print(print_points() == 3)
print("Testing if points increase if correct answer is given")
clue_two_password("runtime")
print(print_points() == 6)
print("Testing if attempts decrease if wrong answer is given")
clue_one_password("runtime")
print(print_increase() == 2)
print("Testing if attempts decrease if wrong answer is given")
clue_two_password("vector")
print(print_increase() == 1)
print("Testing if level increases when points reach threshold")
oldlevel = print_level()
oldpoints = print_points()
get_key_one_for_inventory()
print(print_level() > oldlevel)
print("Testing if points decrease when prize is obtained")
print(print_points() < oldpoints)
print("Testing if prize is obtained in variable")
print(print_keyone() == 1)
