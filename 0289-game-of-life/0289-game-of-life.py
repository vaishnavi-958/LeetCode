from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        # First pass: determine the next state
        for row in range(m):
            for col in range(n):

                live_neighbors = 0

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if 0 <= r < m and 0 <= c < n:
                        # 1 = originally alive
                        # -1 = originally alive, now dead
                        if board[r][c] in (1, -1):
                            live_neighbors += 1

                # Live -> Dead
                if board[row][col] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[row][col] = -1

                # Dead -> Live
                elif board[row][col] == 0:
                    if live_neighbors == 3:
                        board[row][col] = 2

        # Second pass: convert temporary states
        for row in range(m):
            for col in range(n):
                if board[row][col] == -1:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1