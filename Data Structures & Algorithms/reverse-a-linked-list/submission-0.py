# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr is not None:
            forward = curr.next  # Save the next node
            curr.next = prev     # Reverse the pointer
            prev = curr          # Move prev one step forward
            curr = forward       # Move curr one step forward
            
        return prev
            










