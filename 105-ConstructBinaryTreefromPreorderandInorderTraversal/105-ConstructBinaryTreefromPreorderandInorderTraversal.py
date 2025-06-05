# Last updated: 6/5/2025, 3:00:47 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val : idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def dfs(left,right):
            nonlocal pre_idx
            if left > right:
                return None

            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)

            mid = inorder_idx[root_val]

            root.left = dfs(left, mid-1)
            root.right = dfs(mid+1, right)
            
            return root
        

        return dfs(0, len(preorder)-1)
        


