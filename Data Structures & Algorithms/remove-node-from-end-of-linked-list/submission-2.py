# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        length = 0
        current = start
        while current is not None:
            current = current.next
            length += 1

        count = 0
        new_start = ListNode()
        new_head = new_start

        i= 0

        while (count < (length - n)):
            if i ==0:
                new_start.next = start
                new_start = start
                count = count +1
                i = i +1
            else:
                new_start = new_start.next
                count = count +1

        if (length - n) == 0:
            new_start.next = start.next
        else:
            new_start.next = new_start.next.next

        return new_head.next












