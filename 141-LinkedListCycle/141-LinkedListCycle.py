# Last updated: 5/30/2025, 7:34:54 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f, s = head, head
        while f and f.next:
            f = f.next.next
            s = s.next
            if s == f:
                return True
        return False
