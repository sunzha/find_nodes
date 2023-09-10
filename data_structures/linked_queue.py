""" Queue ADT based on linked nodes. """

from data_structures.queue_adt import *

class Node(Generic[T]):
    """ Implementation of a generic Node class.

        Attributes:
            item (T): the data to be stored by the node
            link (Node[T]): reference to the next node
    """

    def __init__(self, item: T = None) -> None:
        """ Object initializer. """
        self.item = item
        self.link = None


class LinkedQueue(Queue[T]):
    """ Implementation of a queue with linked nodes.

        Attributes:
            length (int): number of elements in the queue (inherited)
    """

    def __init__(self, _=None) -> None:
        """ Object initializer. """
        Queue.__init__(self)
        self.front = None
        self.rear = None

    def is_empty(self) -> bool:
        """ Returns whether the queue is empty
            :complexity: O(1)
        """
        return self.front is None

    def append(self, item: T) -> None:
        """ Appends an element to the rear of the queue.
            :complexity: O(1)
        """
        new_node = Node(item)  # create new node
        if self.is_empty():
            self.front = new_node  # move head
        else:
            self.rear.link = new_node  # link it in
        self.rear = new_node  # move rear to new node
        self.length += 1

    def serve(self) -> T:
        """ Serves the element at the front of the queue.
            :pre: queue is not empty
            :complexity: O(1)
            :raises Exception: if the queue is empty
        """
        if not self.is_empty():
            item = self.front.item  # store the item to serve
        self.front = self.front.link  # move front
        self.length -= 1
        if self.is_empty():  # if now empty
            self.rear = None  # move rear
            return item
        else:
            raise ValueError("Queue is empty")
