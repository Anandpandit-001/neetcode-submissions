# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        original_start = head

        while fast.next != None and fast.next.next != None :
            slow = slow.next
            fast = fast.next.next

        list2_start =  slow.next
        slow.next = None
        curr = list2_start
        prev = None

        while ( curr != None):
            forward = curr.next
            curr.next = prev 
            prev = curr
            curr = forward
        
        
        list2_head = prev

        while (original_start != None or list2_head != None):

            original_start_forward = original_start.next
            original_start.next = list2_head
            original_start = original_start_forward

            if list2_head != None:

                list2_head_forward = list2_head.next
                list2_head.next = original_start
                list2_head = list2_head_forward

        













