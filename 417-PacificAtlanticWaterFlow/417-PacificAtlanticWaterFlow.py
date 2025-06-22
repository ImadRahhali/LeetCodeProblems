# Last updated: 6/22/2025, 1:16:32 PM
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [[r-1,c], [r+1,c], [r, c-1], [r, c+1]]
            for i, j in directions:
                if (0 <= i < ROWS and 0 <= j < COLS and (i,j) not in visited and heights[i][j] >= heights[r][c]):
                    dfs(i, j, visited)

        for c in range(COLS):
            dfs(0, c, pacific)               # Starting from Top row and finding cells that can reach Pacific
            dfs(ROWS - 1, c, atlantic)       # Starting from Bottom row and finding cells that can reach Atlantic

        for r in range(ROWS):
            dfs(r, 0, pacific)               # Starting from Left column and finding cells that can reach Pacific
            dfs(r, COLS - 1, atlantic)       # Starting from Right column and finding cells that can reach Atlantic

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic: # collecting cells that can reach both pacific and atlantic
                    res.append([r,c])
        return res
