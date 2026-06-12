# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse
        p, c, t = None, slow, None
        while c:
            t = c.next
            c.next = p

            p = c
            c = t
        
        # merge
        t1 = head
        t2 = p

        while t1 and t2:
            temp1 = t1.next
            temp2 = t2.next

            t1.next = t2
            t2.next = temp1

            t1 = temp1
            t2 = temp2

        return 