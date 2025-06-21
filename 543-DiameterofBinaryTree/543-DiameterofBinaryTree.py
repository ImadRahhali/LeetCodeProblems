# Last updated: 6/21/2025, 12:18:05 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res

            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            res = max(res, left_height+right_height)

            return 1 + max(left_height, right_height)
        
        dfs(root)
        return res

