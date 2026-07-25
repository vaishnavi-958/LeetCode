from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        # Check if first row originally contains a zero
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))

        # Check if first column originally contains a zero
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Use first row and first column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set inner cells to zero based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero the first row if needed
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Zero the first column if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0  