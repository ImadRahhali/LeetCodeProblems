# Last updated: 6/11/2025, 8:32:16 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        tmp = []
        curr = head
        while curr:
            tmp.append(curr.val)
            curr = curr.next

        tmp.reverse()

        dummy = ListNode(0)
        curr = dummy
        for val in tmp:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next