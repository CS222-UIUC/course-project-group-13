from backend_rs import clue_one_password
from backend_rs import clue_two_password
from backend_rs import points
from backend_rs import increase
from backend_rs import level
from backend_rs import get_key_one_for_inventory
from backend_rs import keyone


def test_correct_action(self): #check if points increase properly when correct answer given
    clue_one_password("vector")
    self.assertEqual(points, 3)
    clue_two_password("runtime")
    self.assertEqual(points, 6)

def test_wrong_action(self): #check if tries decrease properly when wrong answer given
    clue_one_password("runtime")
    self.assertEqual(increase, 2)
    clue_two_password("vector")
    self.assertEqual(increase, 1)

def test_inventory_1(self): #check if inventory is correctly updated
    oldlevel = level
    oldpoints = points
    get_key_one_for_inventory()
    self.assertTrue(level > oldlevel)
    self.assertTrue(points < oldpoints)
    self.assertTrue(keyone == 1)
    