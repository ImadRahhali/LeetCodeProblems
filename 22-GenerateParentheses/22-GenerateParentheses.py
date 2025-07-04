# Last updated: 6/22/2025, 10:47:14 AM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(opened, closed):
            if opened == closed == n:
                res.append("".join(stack))
            
            if opened < n:
                stack.append("(")
                backtrack(opened+1, closed)
                stack.pop()
            
            if closed < opened:
                stack.append(")")
                backtrack(opened, closed+1)
                stack.pop()
        
        backtrack(0, 0)
        return res