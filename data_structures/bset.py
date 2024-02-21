"""
    Bivector-based implementation of Set ADT.
"""

from __future__ import annotations
from data_structures.set_adt import Set

class BSet(Set[int]):
    """A bit-vector implementation of the set ADT. The set is represented
        as an integer. The element is present in the set if and only if the
        corresponding bit of the integer is True.

        Attributes:
        elems (int): bitwise representation of the set
    """

    def __init__(self, dummy_capacity: int = 1) -> None:
        """ Initialization. """
        Set.__init__(self)

    def clear(self) -> None:
        """ Makes the set empty. """
        self.elems = 0

    def is_empty(self) -> bool:
        """ True if the set is empty. """
        return self.elems == 0

    def __contains__(self, item: int) -> bool:
        """ True if the set contains the item.
        :raises TypeError: if the item is not integer or if not positive.
        """
        if not isinstance(item, int) or item <= 0:
            raise TypeError('Set elements should be integers')
        return (self.elems >> (item - 1)) & 1

    def __len__(self) -> int:
        """
        Size computation. The most expensive operation.
        Use int.bit_length(your_integer) to calculate the bit length.
        """
        res = 0
        for item in range(1, int.bit_length(self.elems) + 1):
            if item in self:
                res += 1
        return res

    def add(self, item: int) -> None:
        """ Adds an element to the set.
        :raises TypeError: if the item is not integer or if not positive.
        """
        if not isinstance(item, int) or item <= 0:
            raise TypeError('Set elements should be integers')
        self.elems |= 1 << (item - 1)

    def remove(self, item: int) -> None:
        """ Removes an element from the set.
        :raises TypeError: if the item is not integer or if not positive.
        :raises KeyError: if the item is not in the set.
        """
        if not isinstance(item, int) or item <= 0:
            raise TypeError('Set elements should be integers')
        if item in self:
            self.elems ^= 1 << (item - 1)
        else:
            raise KeyError(item)

    def union(self, other: BSet[int]) -> BSet[int]:
        """ Creates a new set equal to the union with another one,
        i.e. the result set should contains the elements of self and other.
        """
        res = BSet()
        res.elems = self.elems | other.elems
        return res

    def intersection(self, other: BSet[int]) -> BSet[int]:
        """ Creates a new set equal to the intersection with another one,
        i.e. the result set should contain the elements that are both in
        self *and* other.
        """
        res = BSet()
        res.elems = self.elems & other.elems
        return res

    def difference(self, other: BSet[int]) -> BSet[int]:
        """ Creates a new set equal to the difference with another one,
        i.e. the result set should contain the elements of self that
        *are not* in other.
        """
        res = BSet()
        res.elems = self.elems & ~other.elems
        return res

    def __len__(self) -> int:
        """
        Size computation. The most expensive operation.
        Use int.bit_length(your_integer) to calculate the bit length.
        """
        return bin(self.elems).count('1')

    def __str__(self):
        """ Construct a nice string representation. """
        bit_elems = self.elems
        out_elems = []
        current = 0
        while bit_elems:
            if bit_elems & (1 << current):
                out_elems.append(str(current+1))
                bit_elems &= ~(1 << current)
            current += 1
        return '{' + ', '.join(out_elems) + '}'

if __name__ == '__main__':
    s = BSet(3)
    s.add(1)
    s.add(4)
    print(f'S = {s}')
    t = BSet(3)
    t.add(4)
    t.add(2)
    t.add(2)
    print(f'T = {t}')

    print(f'S union T = {s.union(t)}')
    print(f'S intersect T = {s.intersection(t)}')
