class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def helperFunc(i , j):
            if i == m or j == n:
                return 0

            if i == m - 1 and j == n -1:
                return 1
            return helperFunc(i + 1, j) + helperFunc(i, j+1)

        return helperFunc(0,0)