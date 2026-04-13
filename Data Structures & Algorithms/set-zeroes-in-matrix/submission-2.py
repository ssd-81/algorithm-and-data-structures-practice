class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        matrix_copy = [row[:] for row in matrix]

        def setzero(r,c):
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if i == r or j == c:
                        matrix[i][j] = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                val = matrix_copy[i][j]
                if val == 0:
                    setzero(i,j)
        
                    

        