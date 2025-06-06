# Last updated: 6/7/2025, 12:53:06 AM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited, queue = set(), deque()
        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i, j))
        if count == 0:
            return 0
            
        minutes = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                directions = [[0,1], [0, -1], [1, 0], [-1,0]]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] == 1 ):
                        queue.append((nr,nc))
                        visited.add((nr, nc))
                        count -= 1
            minutes += 1
        
        return minutes - 1 if count == 0 else -1
