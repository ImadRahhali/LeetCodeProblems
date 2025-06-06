# Last updated: 6/6/2025, 10:36:43 AM
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            visited.add((r, c))

            if r > 0 and heights[r-1][c] >= heights[r][c]:
                dfs(r-1, c, visited)
            if r < ROWS - 1 and heights[r+1][c] >= heights[r][c]:
                dfs(r+1, c, visited)
            if c > 0 and heights[r][c-1] >= heights[r][c]:
                dfs(r, c-1, visited)
            if c < COLS - 1 and heights[r][c+1] >= heights[r][c]:
                dfs(r, c+1, visited)

        for c in range(COLS):
            dfs(0, c, pacific)               # Top row -> Pacific
            dfs(ROWS - 1, c, atlantic)       # Bottom row -> Atlantic

        for r in range(ROWS):
            dfs(r, 0, pacific)               # Left column -> Pacific
            dfs(r, COLS - 1, atlantic)       # Right column -> Atlantic

        return [[r, c] for (r, c) in pacific & atlantic]
