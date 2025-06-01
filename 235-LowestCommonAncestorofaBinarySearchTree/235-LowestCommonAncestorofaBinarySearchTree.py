# Last updated: 6/1/2025, 4:11:40 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def get_val(x):
            return x.val if hasattr(x, 'val') else x

        p_val = get_val(p)
        q_val = get_val(q)
        if p_val == root.val or q_val == root.val:
            return root
        if ((p_val - root.val) * (q_val - root.val) < 0):
            return root
        if p_val < root.val:
            root = root.left
            return self.lowestCommonAncestor(root, p, q)
        if p_val > root.val:
            root = root.right
            return self.lowestCommonAncestor(root, p, q)
            

