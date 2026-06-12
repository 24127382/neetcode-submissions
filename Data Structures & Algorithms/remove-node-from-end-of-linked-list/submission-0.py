# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        t = head
        count = 0
        while t:
            t = t.next
            count += 1

        if count == n:
            return head.next

        t = head
        for _ in range(count - n - 1):
            t = t.next

        t.next = t.next.next

        return head