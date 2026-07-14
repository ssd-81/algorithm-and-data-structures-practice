class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}
        def in_bounds(r,c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def dfs(r, c, prevVal):
            if not in_bounds(r,c) or matrix[r][c] <= prevVal:
                return 0 
            if (r,c) in memo:
                return memo[(r,c)]
            res = 1
            res = max(res, 1 + dfs(r+1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r-1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c+1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c-1, matrix[r][c]))
            memo[(r,c)] = res
            return memo[(r,c)]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, -1)
        return max(memo.values())
