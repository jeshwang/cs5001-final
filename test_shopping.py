"""
Final
===========================
Student:  Jessica Hwang
Semester: Spring 2023
===========================
Testing shopping.py
"""
from shopping import load_item, find_between, correct_spelling, split_string, save_as_shopping_list
from typing import Dict
from shopping_classes import ShoppingList, ListItem
import unittest


class TestListItem(unittest.TestCase):
    def test_load_item(self):
        """Tests load_item()"""
        test_d_correct = {'chiz': 'cheese', 
                'barry': 'berry',
                'burry': 'berry' 
                }
        
        test_d = load_item('test_d.dat')
        self.assertEqual(test_d_correct, test_d)
    

    def test_find_between(self):
        """Tests find_between()"""
        test_1 = 'blah blah start hey test 1 stop'
        test_2 = 'start no stop'
        test_3 = 'hey'
    
        self.assertEqual(find_between(test_1), ' hey test 1 ')
        self.assertEqual(find_between(test_2), ' no ')
        self.assertEqual(find_between(test_3), '')


    def test_correct_spelling(self):
        """Tests correct_spelling"""
        test_d = {'chiz': 'cheese',
                  'barry': 'berry',
                  'burry': 'berry' 
                  }
        
        test_string = 'chiz strings and strawburry'
        self.assertEqual(correct_spelling(raw_list=test_string, d=test_d), 
                         'cheese strings and strawberry')


    def test_correct_spelling_raises_type_error(self):
        """Test the correct_spelling method raises a TypeError"""
        test_d = {'chiz': 'cheese',
                  'barry': 'berry',
                  'burry': 'berry' 
                  }

        with self.assertRaises(TypeError):
            correct_spelling(raw_list=1, d=test_d)
        with self.assertRaises(TypeError):
            correct_spelling(raw_list='test', d=2)


    def test_split_string(self):
        """Tests split_string()"""
        string_1 = 'hello comma my name is comma Mary'
        string_2 = 'she is coma at her house'
        string_3 = 'frank ocean did not livestream and now im sad'

        list_1 = ['hello','my name is', 'Mary']
        list_2 = ['she is', 'at her house']
        list_3 = ['frank ocean did not livestream and now im sad']

        self.assertEqual(split_string(string_1)[0], 'hello')
        self.assertEqual(split_string(string_1)[1], 'my name is')
        self.assertEqual(split_string(string_1)[2], 'Mary')
        self.assertEqual(split_string(string_2)[0], 'she is')
        self.assertEqual(split_string(string_2)[1], 'at her house')
        self.assertEqual(split_string(string_3)[0], 'frank ocean did not livestream and now im sad')


    def test_save_as_shopping_list(self):
        """Tests save_as_shopping_list"""

        test_list = ['1 package of test item 1', '3 bag of test item 2', '1 test item 3']

        # create reference ShoppingList
        test_shop = ShoppingList('shop')

        # create ListItems to fill reference ShoppingList
        item_1 = ListItem(name='test item 1', unit='package')
        item_2 = ListItem(name='test item 2', unit='bag', quantity=3)

        # add ListItems onto reference ShoppingList
        test_shop.add_item(item_1)
        test_shop.add_item(item_2)

        # Start test
        # Create ShoppingList object from test_list
        shopping_list = save_as_shopping_list(test_list)
        # print(shopping_list.get_item(0).__str__())
        print(shopping_list.get_item(1).__str__())
        
        self.assertEqual(shopping_list.get_item(0).__str__(), '1x package of test item 1')
        self.assertEqual(shopping_list.get_item(1).__str__(), '3x bags of test item 2')
    

if __name__ == '__main__':
    unittest.main(verbosity=2)