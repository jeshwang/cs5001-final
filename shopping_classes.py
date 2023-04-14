"""
Final
===========================
Student:  Jessica Hwang
Semester: Spring 2023
===========================
Creates ListItem and ShoppingList classes to use in app.py.

Includes function for writing a ShoppingList object to a .txt file.

Classes included: ListItem, ShoppingList
Functions included: save_list_to_file
"""
from typing import Optional


class ListItem:
    """ListItem class holds the quantity, per unit measure,
    and name of item.

    Attributes:
        quantity (int) - how many units of the item,
            defaults to 1
        unit(str) - per-unit name of the item (e.g., carton, bag), 
            defaults to the empty string ''
        name (str) - name of item 
    """
    def __init__(self, name: str, unit: str='', quantity: int=1):
        """Constructor of the ListItem object. 

        Args:
            name (str) - name of item 
            unit(str) - per-unit name of the item (like carton, bag), 
                defaults to the empty string ''
            quantity (int) - how many units of the item,
                defaults to 1
        """
        self.name = name
        self.unit = unit
        self.quantity = quantity


    def __str__(self) -> str:
        """Returns a string representation of the object 
        in the format: 
        'quantityX unit name" for quantity of 1
        'quantityX units name" for quantity > 1
        """
        if self.unit == '':
            return f"{self.quantity}x {self.name}"
        else:  # unit is plural if quantity > 1
            if self.quantity > 1:
                return f"{self.quantity}x {self.unit}s of {self.name}"
            else:
                return f"{self.quantity}x {self.unit} of {self.name}"


class ShoppingList:
    """
    The ShoppingList class is a collection of ListItem objects.

    Attributes:
        name (str) - the name of the list. 
            This is public/able to modified directly. 
            Default to "New List" if no name is provided.
        items (list) - this should be a private property that is 
            a list of ListItem objects. It should be initialized to an empty list. 
            At no point should anyone be able to access the items outside of the class.
    """
    def __init__(self, name='New List', items=[]):
        """
        Constructor of ToDoList

        Args:
            name (str): name of list
            items (list): list of ListItem objects
        """
        self.name = name
        self.__items = items.copy()

    @property
    def items(self) -> list:
        """Returns list of ListItem objects"""
        return self.__items

    def size(self) -> int:
        """Returns the total number of items in the list"""
        return len(self.__items)

    def add_item(self, item: ListItem):
        """Adds an item to the list. 
        It should check to make sure the item is a ListItem object, 
        and if not, raise a TypeError. 
        """
        if not isinstance(item, ListItem):
            raise TypeError("item must be a ListItem")
        self.__items.append(item)

    def remove_item(self, item: ListItem):
        """Removes an item from the list.
        """
        self.__items.remove(item)

    def get_item(self, index: int):
        """ Returns the item at the specified index. 
        If the index is out of range, it should raise an IndexError
          (which is the default behavior of python lists)."""
        return self.__items[index]

    def find_item(self, short_name: str) -> Optional[ListItem]:
        """Returns the first item in the list that matches the 
        short_name. If no item is found, it should return None. 
        If you are choosing to use typing for a return type, 
        you can use the optional typing syntax to indicate that 
        it can return None. """
        for i in range(0, len(self.__items)):
            if self.__items[i].short_name.lower() == short_name.lower():
                return self.__items[i]
        return None

    def __str__(self) -> str:
        """Returns a string representation of the list. 
        However, in this case, it will only print the list name
        and number of items in the following format. 
        With name replaced by the name of the list, and 
        # replaced by the number of items in the list: 
        Name (# items)
        """
        return f"{self.name} ({self.size()} items)"


def save_list_to_file(list: ShoppingList) -> None:
    """Write a ShoppingList object to a file. 
    The file name should be the name of the list, 
    with a .txt extension. 

    Args:
        list (ShoppingList): list of ListItems

    Return: None
    """
    # create new .txt file
    my_file_name = list.name + ".txt"

    # start writing in .txt file
    my_file = open(my_file_name, 'w')

    length = list.size()

    # add the ShoppingList name and quantity of items total
    # as the first line in the file
    my_file.write(list.__str__() + "\n")

    for i in range(0, length):
        # create a string representing ListItem to add to file
        new_entry = list.get_item(i).__str__()

        # add print breaks after each item except for last item
        if i < (length - 1):
            my_file.write(new_entry + "\n")
        if i == (length - 1):
            my_file.write(new_entry)

    my_file.close()
