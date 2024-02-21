""" List ADT. Defines a generic abstract list with the standard methods. """

from abc import ABC, abstractmethod
from typing import TypeVar, Generic
T = TypeVar('T')

__author__ = 'Maria Garcia de la Banda and Brendon Taylor. Modified by Alexey Ignatiev'
__docformat__ = 'reStructuredText'

class List(ABC, Generic[T]):
    """ Abstract class for a generic List. """
    def __init__(self) -> None:
        """ Basic List object initialiser. """
        self.length = 0

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        """ Magic method. Return the element at a given position. """
        pass

    @abstractmethod
    def __setitem__(self, index: int, item: T) -> None:
        """ Magic method. Insert the item at a given position. """
        pass

    def __len__(self) -> int:
        """ Return the size of the list. """
        return self.length

    def __str__(self):
        """ Magic method constructing a string representation of the list object. """
        result = '['
        for i in range(len(self)):
            if i > 0:
                result += ', '
            result += str(self[i]) if type(self[i]) != str else "'{0}'".format(self[i])
        result += ']'
        return result

    def append(self, item: T) -> None:
        """ Append a new item to the end of the list. """
        self.insert(len(self), item)

    @abstractmethod
    def insert(self, index: int, item: T) -> None:
        """ Insert an item at a given position. """
        pass

    def remove(self, item: T) -> None:
        """ Remove an item from the list. """
        index = self.index(item)
        self.delete_at_index(index)

    @abstractmethod
    def delete_at_index(self, index: int) -> T:
        """ Delete item at a given position. """
        pass

    @abstractmethod
    def index(self, item: T) -> int:
        """ Find the position of a given item in the list. """
        pass

    def is_empty(self) -> bool:
        """ Check if the list of empty. """
        return len(self) == 0

    def clear(self):
        """ Clear the list. """
        self.length = 0
