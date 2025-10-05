
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS-1])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])
    
                return
            visit.add((r,c))
prevHeight > heights[r][c]):
            if ((r,c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or 
        def dfs(r, c, visit, prevHeight):

        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
class Solution: