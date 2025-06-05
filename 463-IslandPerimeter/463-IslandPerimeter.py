# Last updated: 6/5/2025, 8:40:33 PM
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(r, c):
            if min(r,c) < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 1
            if (r,c) in visited:
                return 0
            
            counter = 0
            visited.add((r,c))

            counter += dfs(r-1, c)
            counter += dfs(r+1, c)
            counter += dfs(r, c-1)
            counter += dfs(r, c+1)

            return counter 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i,j)