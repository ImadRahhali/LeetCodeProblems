# Last updated: 6/2/2025, 11:10:12 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, max_val):
            nonlocal count
            if not node:
                return count
            
            if node.val >= max_val:
                count += 1
            
            max_val = max(max_val, node.val)
            dfs(node.left, max_val)
            dfs(node.right, max_val)
        
        dfs(root, root.val)
        return count

        