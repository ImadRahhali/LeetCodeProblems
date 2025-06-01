# Last updated: 6/1/2025, 5:05:19 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def findMax(root):
            curr = root
            while curr and curr.right:
                curr = curr.right
            return curr
        
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            if not root.left:
                 return root.right
            elif not root.right:
                 return root.left
            else:
                maxNode = findMax(root.left)
                root.val = maxNode.val
                root.left = self.deleteNode(root.left, maxNode.val)
        return root

        

            