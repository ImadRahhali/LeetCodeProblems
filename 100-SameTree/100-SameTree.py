# Last updated: 6/2/2025, 9:43:30 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def isSame(node1, node2):
            if not node1 and node2:
                return False
            if not node2 and node1:
                return False
            if not node1 and not node2:
                return True
            isRoot = (node1.val == node2.val)
            isLeft=  isSame(node1.left,node2.left)
            isRight = isSame(node1.right, node2.right)

            return isRoot and isLeft and isRight
        
        return isSame(p,q)