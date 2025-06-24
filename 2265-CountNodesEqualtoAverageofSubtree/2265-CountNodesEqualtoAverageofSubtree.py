# Last updated: 6/24/2025, 8:42:14 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return [0,0]
            left = dfs(node.left)
            right = dfs(node.right)
            if (node.val + left[0] + right[0])//(1+left[1]+right[1]) == node.val:
                res += 1
            return [node.val + left[0] + right[0],1+left[1]+right[1]]
        dfs(root)
        return res
            
