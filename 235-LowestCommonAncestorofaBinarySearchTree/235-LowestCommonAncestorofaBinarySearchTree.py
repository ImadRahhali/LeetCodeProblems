# Last updated: 6/1/2025, 4:17:49 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:
            if p.val > curr.val and q.val>curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val<curr.val:
                curr = curr.left
            else:
                return curr

