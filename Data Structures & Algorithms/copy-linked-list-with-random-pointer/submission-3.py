"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cloned = {}

        def clone(node):
            if not node:
                return None
            
            # If we already cloned this node in a previous step,
            # just return that clone to avoid infinite recursion!
            if node in cloned:
                return cloned[node]
            
            # Create a copy of the current node
            new_node = Node(node.val)
            # Register it in our map BEFORE making recursive calls
            cloned[node] = new_node
            
            # Recursively copy the next and random pointers
            new_node.next = clone(node.next)
            new_node.random = clone(node.random)
            
            return new_node

        return clone(head)
