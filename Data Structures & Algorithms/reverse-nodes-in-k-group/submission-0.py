# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        length = 0
        while(start != None):
            length = length + 1
            start = start.next
        loop_count = length // k

        curr = head
        origin = head
        previous_pointer_location = origin
        output_head = origin

        for i in range (loop_count):

            for j in range (k - 1):
                curr = curr.next

            new_start = curr.next

            prev = None
            loop_curr = origin
            

            while(prev != curr):
                forward = loop_curr.next
                loop_curr.next = prev
                prev = loop_curr
                loop_curr = forward

            if i == 0:
                output_head = prev

            if i != 0:
                previous_pointer_location.next = curr

            if new_start != None:
                previous_pointer_location = origin
                origin = new_start
                curr = new_start

            if new_start != None:
                previous_pointer_location.next =  new_start
                
        return output_head  


            











        