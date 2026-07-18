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
        dictionary_Nodes = {}
        if head is None:
            return None

        start = head
        head_val = head.val
        new_head = Node(head_val)

        dictionary_Nodes[head] = new_head

        new_head_pointer = new_head
        head = head.next

        while(head != None):
            head_val = head.val
            new_node = Node(head_val)
            dictionary_Nodes[head] = new_node
            new_head.next = new_node
            new_head = new_node
            head = head.next

        while(start != None):
            if start.random  is not None:
                location_of_random = start.random
                first_pointer = dictionary_Nodes[start]
                second_pointer = dictionary_Nodes[location_of_random]
                first_pointer.random = second_pointer

            start = start.next

        return new_head_pointer

        







        











