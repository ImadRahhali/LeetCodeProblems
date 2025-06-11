# Last updated: 6/11/2025, 9:08:16 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        dummy = ListNode(0, prev)
        curr = dummy
        while n > 1 and curr:
            curr = curr.next
            n -= 1
        curr.next = curr.next.next

        prev, curr = None, dummy.next
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev