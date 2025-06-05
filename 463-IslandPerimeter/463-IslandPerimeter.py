# Last updated: 6/5/2025, 7:45:08 PM
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    continue
                else:
                    if r == 0 or grid[r-1][c] == 0:
                        count += 1
                    if r == len(grid) - 1 or grid[r+1][c] == 0:
                        count += 1
                    if c == 0 or grid[r][c-1] == 0:
                        count += 1
                    if c == len(grid[0]) - 1 or grid[r][c+1] == 0:
                        count += 1
        return count