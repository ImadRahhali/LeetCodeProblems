# Last updated: 6/5/2025, 7:56:00 PM
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                edges = 0
                if grid[r][c] == 1:
                    edges = 4
                    if r > 0 and grid[r-1][c] == 1:
                        edges -= 1
                    if r < len(grid) - 1 and grid[r+1][c] == 1:
                        edges -= 1
                    if c > 0 and grid[r][c-1] == 1:
                        edges -= 1
                    if c < len(grid[0]) - 1 and grid[r][c+1] == 1:
                        edges -= 1
                count += edges
        return count