# Last updated: 6/1/2025, 4:54:47 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

# find it :
# if 0 child remove it take the assigned pointer to none
# if 1 child take the assigned pointer to that child

# if 2 childs then replace the node with the minimum val in its right sub tree or the maximum in its left sub tree

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

        

            