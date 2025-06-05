# Last updated: 6/5/2025, 9:39:09 PM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_count = 0
        def dfs(r, c):
            if min(r,c) < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            count = 1
            count += dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
            return count
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_count = max(max_count, dfs(i, j))
        return max_count
        