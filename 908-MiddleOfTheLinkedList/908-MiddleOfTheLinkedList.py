# Last updated: 5/30/2025, 7:34:21 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = head
        f = head
        while f and f.next:
            f = f.next.next
            s = s.next
        return s