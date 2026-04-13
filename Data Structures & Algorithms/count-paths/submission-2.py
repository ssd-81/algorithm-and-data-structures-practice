class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # get used to this, man
        cache = [[0 for _ in range(n)] for _ in range(m)]
        def helperFunc(i , j):
            if i == m or j == n:
                return 0

            if i == m - 1 and j == n -1:
                cache[i][j] = 1
                return 1
            
            if cache[i][j] != 0:
                return cache[i][j]
            return helperFunc(i + 1, j) + helperFunc(i, j+1)

        return helperFunc(0,0)