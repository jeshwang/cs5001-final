"""
Final
===========================
Student:  Jessica Hwang
Semester: Spring 2023
===========================
Testing List Item class from shopping_classes.py
"""
from typing import Optional
import unittest
from shopping_classes import ListItem


class TestListItem(unittest.TestCase):
    def test___str__(self):
        """Tests __str__(self)"""
        item_1 = ListItem(name='test')
        self.assertEqual(item_1.__str__(), "1x test")
        
        item_2 = ListItem(name='cheese', unit='package', quantity=4)
        self.assertEqual(item_2.__str__(), "4x packages of cheese")

        item_3 = ListItem(name='orange', unit='bag', quantity=1)
        self.assertEqual(item_3.__str__(), "1x bag of orange")


if __name__ == '__main__':
    unittest.main(verbosity=2)