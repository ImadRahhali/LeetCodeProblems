# Last updated: 6/6/2025, 9:58:31 AM
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
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

        for j in range(COLS):
            dfs(0, j, pacific)               # Top row -> Pacific
            dfs(ROWS - 1, j, atlantic)       # Bottom row -> Atlantic

        for i in range(ROWS):
            dfs(i, 0, pacific)               # Left column -> Pacific
            dfs(i, COLS - 1, atlantic)       # Right column -> Atlantic

        return [[r, c] for (r, c) in pacific & atlantic]
