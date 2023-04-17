"""
Final
===========================
Student:  Jessica Hwang
Semester: Spring 2023
===========================
Contains functions used in app.py to generate a simple shopping list
from the transcript of an audio file.

Functions include:
load_item
find_between
correct_spelling
split_string
save_as_shopping_list
"""
import re
import os
from typing import Dict
from shopping_classes import ShoppingList, ListItem
from shopping_classes import save_list_to_file


def load_item(filename: str) -> Dict[str, str]:
    """Loads items from the given file and returns a 
    dictionary of items with common mispellings of that item
    and the correct spelling.

    Assumption: all items are written fully in lowercase

    Example:
        >>> load_item("item.dat")
        {'carat':'carrot',
        'carats':'carrots'
        }

    Args:
        filename (str): The name of the file to load the quantities from.

    Returns:
        Dict[str, str]: A dictionary of commonly mispelled items and 
            their correct spellings
    """
    my_list = {}
    
    try:
        with open(filename, "r") as file:
            for line in file:
                key = line[:line.index(":")]  # get key
                val = line[line.index(":")+1:].strip('\n')
                my_list[key] = val
        return my_list
    except FileNotFoundError:
        print("Dictionary file is not found!")
    except OSError as a:
        print(a)


def find_between(sample: str, start: str='start', stop: str='stop') -> str:
    """ Takes in the string representing the transcript from 
    an audio file. Returns only the substring between two
    marker words: start and stop.

    Args:
        sample (str): transcript from audio file
        start (str): indicator representing start of list
        stop (str): indicator representing end of list
    Return:
        str: return 
    """
    try:
        first = sample.index(start) + len(start)
        last = sample.index(stop, first)
        subsample = sample[first:last]
        return subsample
    except ValueError:
        return ''


def correct_spelling(raw_list: str, d: Dict[str, str]) -> str:
    """ Takes in a string representing
    info to be placed into a shopping list.
    Corrects the spelling of commonly mispelled terms using
    a dictionary like item.dat, quantity.dat.

    Args:
        raw_list (str): long string from audio transcription
        d (Dict[str, str]): dictionary with keys representing
            common mispellings and values representing the relevant
            word spelled correctly. There can be multiple keys
            with the same value, but there are no multiple values
            with the same key.
    Returns:
        str: long string with correct spellings
    """
    if type(raw_list) != str:
        raise TypeError('raw_list is not a string.')
    elif type(d) != dict:
        raise TypeError('d is not a dictionary type.')
    else:
        for key, value in d.items():
            raw_list = raw_list.replace(key, value)
        return raw_list


def split_string(raw: str) -> list:
    """ Splits a long string into a list of substrings.
    Each substring should contain info about the name of item,
    and its associated quantity and unit.

    Assumption: the keyword "comma" is used at the end of
        a phrase to indicate that the user is done talking about
        the current item, and will talk about the next item.
    Args:
        raw (str): the long string ouputted
        from the recording of the list.
    Return:
        list of strings: substrings containing info about each item
    """
    if type(raw) != str:
        raise TypeError('Argument must be a string.')
    else:
        # split list by "comma" or "coma"
        raw_list = raw.replace('coma','comma').split('comma')

        # for each element in list, remove extra spaces
        raw_list = ["".join(x.strip()) for x in raw_list]

        return raw_list


def save_as_shopping_list(raw_list: list[str]) -> ShoppingList:
    """Reads in a list of strings, where each string contains an
    item and details about the item. Creates a ListItem object
    for each string. Adds each ListItem object into a ShoppingList
    object.

    Example of turning a string into a ListItem:
        "1 pack of chicken legs" turns into a ListItem
        object with name='chicken legs', quantity=1, and
        unit='pack'
    
    Assumptions:
        Each string contains, in this order: details about the
        quantity first, then the unit, and finally the item name.
    Args:
        raw_list (list[str]): list of strings, where each string
        contains an item and details about the item.
    Returns:
        ShoppingList: a ShoppingList containing ListItems, where
        each ListItem reprents an item, its quantity, and unit of 
        measurement (when relevant).
    """
    if type(raw_list) != list:
        raise TypeError('Argument is not a list.')
    else:
        # create ShoppingList object
        my_shopping_list = ShoppingList()

        # for every string in raw_list, turn string into a ListItem, and
        # add ListItem to the ShoppingList
        for i in raw_list:
            item_quant = int(i[0])  # extract quantity
            words = i[2:]
            if " of " in words:
                split_words = words.split(" of ")
                item_unit = split_words[0].strip()  # extract unit
                item_name = split_words[1].strip()  # extract name
            else:
                item_unit = ''
                item_name = words.strip()
            # create ListItem
            my_item = ListItem(name=item_name, unit=item_unit, quantity=item_quant)
            # add ListItem to the ShoppingList
            my_shopping_list.add_item(item=my_item)

        return my_shopping_list
 