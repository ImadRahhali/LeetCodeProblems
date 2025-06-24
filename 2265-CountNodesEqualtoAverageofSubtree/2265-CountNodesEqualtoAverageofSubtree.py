# Last updated: 6/24/2025, 8:44:04 PM
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
            sum_of_values = node.val + left[0] + right[0]
            number_of_nodes = 1 + left[1] + right[1]
            if sum_of_values // number_of_nodes == node.val:
                res += 1
            return [sum_of_values , number_of_nodes]
        dfs(root)
        return res
            
