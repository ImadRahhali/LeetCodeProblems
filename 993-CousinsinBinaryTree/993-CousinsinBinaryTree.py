# Last updated: 6/7/2025, 12:58:04 AM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fresh_count, minutes = 0, 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        directions = [[0,1], [0, -1], [1, 0], [-1,0]]

        while fresh_count > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1 ):
                        queue.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh_count -= 1
            minutes += 1
        
        return minutes if fresh_count == 0 else -1
