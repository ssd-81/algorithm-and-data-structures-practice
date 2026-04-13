class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        level_val = [1 for _ in range(n)]
        for i in range(m - 2 , -1, -1):

            for j in range(n-2, -1, -1):
                level_val[j] = level_val[j] + level_val[j+1]
        
        return level_val[0]
