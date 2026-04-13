class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[0] * n for _ in range(m)]

        def helperFunc(i, j):
            if i == m or j == n:
                return 0 
            
            if obstacleGrid[i][j] == 1:
                return 0 

            if i == m - 1 and j == n -1 :
                cache[i][j] = 1
                return 1
            
            if cache[i][j] != 0:
                return cache[i][j]
            cache[i][j] = helperFunc(i + 1, j) + helperFunc(i, j + 1)
            return cache[i][j]
        
        return helperFunc(0, 0)