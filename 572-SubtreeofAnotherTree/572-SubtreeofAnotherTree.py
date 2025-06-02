# Last updated: 6/2/2025, 12:18:36 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(node1, node2):
            if not node1 or not node2:
                return node1 == node2
            if node1.val != node2.val:
                return False
            return isSame(node1.left, node2.left) and isSame(node1.right, node2.right)

        if not root:
            return False
        
        return isSame(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

            