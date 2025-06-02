# Last updated: 6/2/2025, 10:43:15 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()

        if root:
            queue.append(root)
        while queue:
            level = [0] * len(queue)
            for i in range(len(level)):
                curr = queue.popleft()
                level[i] = curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(level)      
        return res
            
                


