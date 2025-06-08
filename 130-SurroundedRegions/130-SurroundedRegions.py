# Last updated: 6/8/2025, 12:05:28 PM
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or board[r][c] != 'O'):
                return
            board[r][c] = 'S'
            for dr, dc in neighbors:
                dfs(r + dr, c + dc)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'S':
                    board[i][j] = 'O'
        
            