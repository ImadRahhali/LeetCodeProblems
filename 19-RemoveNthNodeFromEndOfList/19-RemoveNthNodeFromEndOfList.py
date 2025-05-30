# Last updated: 5/30/2025, 7:35:16 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = left
        count = 0
        while count < n +1:
            right = right.next
            count+=1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next