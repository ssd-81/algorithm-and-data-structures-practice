class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_row = set()
        zero_cols = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_cols.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zero_row or j in zero_cols:
                    matrix[i][j] = 0
        
        