""" Queue ADT and an array implementation.

Defines a generic abstract queue with the usual methods, and implements
a circular queue using arrays. Also defines UnitTests for the class.
"""
__author__ = "Maria Garcia de la Banda for the base"+"XXXXX student for"
__docformat__ = 'reStructuredText'

import unittest
from abc import ABC, abstractmethod
from typing import Generic
from data_structures.referential_array import ArrayR, T

class Queue(ABC, Generic[T]):
    """ Abstract class for a generic Queue. """

    def __init__(self) -> None:
        self.length = 0

    @abstractmethod
    def append(self,item:T) -> None:
        """ Adds an element to the rear of the queue."""
        pass

    @abstractmethod
    def serve(self) -> T:
        """ Deletes and returns the element at the queue's front."""
        pass

    def __len__(self) -> int:
        """ Returns the number of elements in the queue."""
        return self.length

    def is_empty(self) -> bool:
        """ True if the queue is empty. """
        return len(self) == 0

    @abstractmethod
    def is_full(self) -> bool:
        """ True if the stack is full and no element can be pushed. """
        pass

    def clear(self):
        """ Clears all elements from the queue. """
        self.length = 0

class CircularQueue(Queue[T]):
    """ Circular implementation of a queue with arrays.

    Attributes:
         length (int): number of elements in the stack (inherited)
         front (int): index of the element at the front of the queue
         rear (int): index of the first empty space at the back of the queue
         array (ArrayR[T]): array storing the elements of the queue

    ArrayR cannot create empty arrays. So MIN_CAPACITY used to avoid this.
    """
    MIN_CAPACITY = 1

    def __init__(self,max_capacity:int) -> None:
        Queue.__init__(self)
        self.front = 0
        self.rear = 0
        self.array = ArrayR(max(self.MIN_CAPACITY,max_capacity))


    def append(self, item: T) -> None:
        """ Adds an element to the rear of the queue.
        :pre: queue is not full
        :raises Exception: if the queue is full
        """
        if self.is_full():
            raise Exception("Queue is full")

        self.array[self.rear] = item
        self.length += 1
        self.rear = (self.rear + 1) % len(self.array)

    def serve(self) -> T:
        """ Deletes and returns the element at the queue's front.
        :pre: queue is not empty
        :raises Exception: if the queue is empty
        """
        if self.is_empty():
            raise Exception("Queue is empty")

        self.length -= 1
        item = self.array[self.front]
        self.front = (self.front+1) % len(self.array)
        return item

    def is_full(self) -> bool:
        """ True if the queue is full and no element can be appended. """
        return len(self) == len(self.array)

    def clear(self) -> None:
        """ Clears all elements from the queue. """
        Queue.__init__(self)
        self.front = 0
        self.rear = 0


class TestQueue(unittest.TestCase):
    """ Tests for the above class."""
    EMPTY = 0
    ROOMY = 5
    LARGE = 10
    CAPACITY = 20

    def setUp(self):
        self.lengths = [self.EMPTY, self.ROOMY, self.LARGE, self.ROOMY, self.LARGE]
        self.queues = [CircularQueue(self.CAPACITY) for i in range(len(self.lengths))]
        for queue, length in zip(self.queues, self.lengths):
            for i in range(length):
                queue.append(i)
        self.empty_queue = self.queues[0]
        self.roomy_queue = self.queues[1]
        self.large_queue = self.queues[2]
        #we build empty queues from clear.
        #this is an indirect way of testing if clear works!
        #(perhaps not the best)
        self.clear_queue = self.queues[3]
        self.clear_queue.clear()
        self.lengths[3] = 0
        self.queues[4].clear()
        self.lengths[4] = 0

    def tearDown(self):
        for s in self.queues:
            s.clear()

    def test_init(self):
        self.assertTrue(self.empty_queue.is_empty())
        self.assertEqual(len(self.empty_queue), 0)

    def test_len(self):
        """ Tests the length of all queues created during setup."""
        for queue, length in zip(self.queues, self.lengths):
            self.assertEqual(len(queue), length)

    def test_is_empty_add(self):
        """ Tests queues that have been created empty/non-empty."""
        self.assertTrue(self.empty_queue.is_empty())
        self.assertFalse(self.roomy_queue.is_empty())
        self.assertFalse(self.large_queue.is_empty())

    def test_is_empty_clear(self):
        """ Tests queues that have been cleared."""
        for queue in self.queues:
            queue.clear()
            self.assertTrue(queue.is_empty())

    def test_is_empty_serve(self):
        """ Tests queues that have been served completely."""
        for queue in self.queues:
            #we empty the queue
            try:
                while True:
                    was_empty = queue.is_empty()
                    queue.serve()
                    #if we have served without raising an assertion,
                    #then the queue was not empty.
                    self.assertFalse(was_empty)
            except:
                self.assertTrue(queue.is_empty())

    def test_is_full_add(self):
        """ Tests queues that have been created not full."""
        self.assertFalse(self.empty_queue.is_full())
        self.assertFalse(self.roomy_queue.is_full())
        self.assertFalse(self.large_queue.is_full())

    def test_append_and_serve(self):
        for queue in self.queues:
            nitems = self.ROOMY
            for i in range(nitems):
                queue.append(i)
            for i in range(nitems):
                self.assertEqual(queue.serve(), i)

    def test_clear(self):
        for queue in self.queues:
            queue.clear()
            self.assertEqual(len(queue), 0)
            self.assertTrue(queue.is_empty())

if __name__ == '__main__':
    testtorun = TestQueue()
    suite = unittest.TestLoader().loadTestsFromModule(testtorun)
    unittest.TextTestRunner().run(suite)
