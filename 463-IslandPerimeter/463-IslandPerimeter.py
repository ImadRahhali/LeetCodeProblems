# Last updated: 6/5/2025, 8:22:18 PM
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(r, c, grid, visited):
            if min(r,c) < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 1
            if (r,c) in visited: 
                return 0
            
            visited.add((r,c))
            count = 0

            count += dfs(r-1, c, grid, visited)
            count += dfs(r+1, c, grid, visited)
            count += dfs(r, c-1, grid, visited)
            count += dfs(r, c+1, grid, visited)

            return count
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j , grid, set())

