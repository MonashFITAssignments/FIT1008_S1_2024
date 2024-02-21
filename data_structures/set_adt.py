"""
    Set ADT. Defines a generic abstract set with the usual methods.
"""

from __future__ import annotations

__author__ = "Alexey Ignatiev"
__docformat__ = 'reStructuredText'

from abc import ABC, abstractmethod
from typing import TypeVar, Generic
T = TypeVar('T')

class Set(ABC, Generic[T]):
    """ Abstract class for a generic Set. """

    def __init__(self) -> None:
        """ Initialization. """
        self.clear()

    @abstractmethod
    def __len__(self) -> int:
        """ Returns the number of elements in the set. """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """ True if the set is empty. """
        pass

    @abstractmethod
    def clear(self) -> None:
        """ Makes the set empty. """
        pass

    @abstractmethod
    def __contains__(self, item: T) -> bool:
        """ True if the set contains the item. """
        pass

    @abstractmethod
    def add(self, item: T) -> None:
        """ Adds an element to the set. Note that an element already
        present in the set should not be added.
        """
        pass

    @abstractmethod
    def remove(self, item: T) -> None:
        """ Removes an element from the set. An exception should be
        raised if the element to remove is not present in the set.
        """
        pass

    @abstractmethod
    def union(self, other: Set[T]) -> Set[T]:
        """ Makes a union of the set with another set. """
        pass

    @abstractmethod
    def intersection(self, other: Set[T]) -> Set[T]:
        """ Makes an intersection of the set with another set. """
        pass

    @abstractmethod
    def difference(self, other: Set[T]) -> Set[T]:
        """ Creates a difference of the set with another set. """
        pass
