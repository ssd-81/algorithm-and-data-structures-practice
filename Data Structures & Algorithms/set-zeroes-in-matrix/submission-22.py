class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        row_contains_zero = False
        col_contains_zero = False

        for c in range(COLS):
            if matrix[0][c] == 0:
                row_contains_zero = True
                break
        
        for r in range(ROWS):
            if matrix[r][0] == 0:
                col_contains_zero = True
                break

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0 
                    matrix[0][c] = 0
        print(matrix)
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        print("0x0x0x0x0x0x")
        print(matrix)
        if row_contains_zero:
            for c in range(COLS):
                matrix[0][c] = 0
        if col_contains_zero:
            for r in range(ROWS):
                matrix[r][0] = 0

        