class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return 
        
        flagCheck = set()

        m = len(matrix)
        n = len(matrix[0])

        first_row_contains = False
        first_col_contains = False
        for i in range(m):
            for j in range(n):
                if i == 0  and matrix[i][j] == 0:
                    first_row_contains = True
                if j == 0 and matrix[i][j] == 0:
                    first_col_contains = True
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        print(first_row_contains)
        print(first_col_contains)
        for i in range(m):
            for j in range(n):
                if first_row_contains:
                    if i == 0:
                        matrix[i][j] = 0
                if first_col_contains:
                    if j == 0:
                        matrix[i][j] = 0

        