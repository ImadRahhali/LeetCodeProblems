# Last updated: 6/6/2025, 10:43:46 AM
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visited):
            visited.add((r, c))
            directions = [[r-1,c], [r+1,c], [r, c-1], [r, c+1]]
            for i, j in directions:
                if (
                    0 <= i < ROWS and
                    0 <= j < COLS and
                    heights[i][j] >= heights[r][c] and
                    (i,j) not in visited
                    ):
                    
                    dfs(i, j, visited)

        for c in range(COLS):
            dfs(0, c, pacific)               # Top row -> Pacific
            dfs(ROWS - 1, c, atlantic)       # Bottom row -> Atlantic

        for r in range(ROWS):
            dfs(r, 0, pacific)               # Left column -> Pacific
            dfs(r, COLS - 1, atlantic)       # Right column -> Atlantic

        return [[r, c] for (r, c) in pacific & atlantic]
