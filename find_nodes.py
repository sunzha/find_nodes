from __future__ import annotations
from dataclasses import dataclass

from data_structures.linked_stack import LinkedStack
from data_structures.linked_queue import LinkedQueue

@dataclass
class GNode:
    """ A Node which stores data an integer and has pointers to nodes it is connected to

    Instance Attributes
    -------------------
    val (int):
        The value of the current node
    next (list[GNode] or None):
        The nodes it is connected to, None if it has no connections
    """
    val: int
    next: list[GNode]|None = None

def find_node_recursion(head: GNode, end_val: int) -> GNode:
    """ Finds a node with the specified value in the graph recursively
    
    :Input:
        head (GNode): The node to start looking from
        end_val (int): The node to find
    
    :Returns:
        GNode: The node with which has end_val as its value
    """
    # base case: current node is the node we are looking for
    #           or the current node has no further connections
    if head.val == end_val:
        return head
    elif head.next == None:
        return None
    
    # for each one of the neighbours in the current node
    for neighbours in head.next:
        # call the function recursively to try to find the node specified
        node = find_node_recursion(neighbours, end_val)
        if node != None:
            return node

def find_node(head: GNode, end_val: int) -> GNode:
    """ Finds a node with the specified value in the graph iteratively
    
    :Input:
        head (GNode): The node to start looking from
        end_val (int): The node to find
    
    :Returns:
        GNode: The node with which has end_val as its value
    """
    # add your solution here, should not use recursion

if __name__ == "__main__":
    nodes = [GNode(i) for i in range(9)]
    nodes[0].next = [nodes[i] for i in [1, 3, 6]]
    nodes[1].next = [nodes[i] for i in [2]]
    nodes[2].next = None
    nodes[3].next = [nodes[i] for i in [4]]
    nodes[4].next = [nodes[i] for i in [5]]
    nodes[5].next = None
    nodes[6].next = [nodes[i] for i in [7, 8]]
    nodes[7].next = [nodes[i] for i in [4]]
    nodes[8].next = None
    head = nodes[0]
    
    for node in nodes:
        print(f"Trying to find node {node.val}, found: {find_node(head, node.val).val}")