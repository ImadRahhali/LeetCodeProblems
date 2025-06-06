# Last updated: 6/6/2025, 7:59:12 PM
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        queue.append((0, 0))
        visited.add((0, 0))

        length = 1
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                directions = [[0,1], [0, -1], [1, 0], [-1,0], [1,1], [-1,-1], [1,-1], [-1,1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if ( 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] == 0):
                        queue.append((nr,nc))
                        visited.add((nr,nc))
            length += 1
        
        return -1


