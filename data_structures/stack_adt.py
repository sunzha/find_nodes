"""
    Stack ADT and an array implementation. Defines a generic abstract
    stack with the usual methods.
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic
T = TypeVar('T')


class Stack(ABC, Generic[T]):
    """ Abstract Stack class. """
    def __init__(self) -> None:
        """ Object initializer. """
        self.length = 0

    @abstractmethod
    def push(self, item: T) -> None:
        """ Pushes an element to the top of the stack."""
        pass

    @abstractmethod
    def pop(self) -> T:
        """ Pops an element from the top of the stack."""
        pass

    def __len__(self) -> int:
        """ Returns the number of elements in the stack."""
        return self.length

    def is_empty(self) -> bool:
        """ Returns True iff the stack is empty. """
        return len(self) == 0
