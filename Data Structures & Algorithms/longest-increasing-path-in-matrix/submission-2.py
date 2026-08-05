class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        memo = {}
        rows, cols = len(matrix), len(matrix[0])

        def in_bound(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c):
            if (r,c) in memo:
                return memo[(r,c)]
            max_cover = 1
            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc
                if in_bound(new_r, new_c) and matrix[new_r][new_c] > matrix[r][c]:
                    max_cover = max(max_cover, 1 + dfs(new_r, new_c))
            memo[(r,c)] = max_cover 
            return memo[(r,c)]


        
        longest_inc_path = float('-inf')
        for r in range(rows):
            for c in range(cols):
                longest_inc_path = max(longest_inc_path, dfs(r,c))
        return longest_inc_path 