class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def in_bounds(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        visited = set()
        max_area = 0 
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def dfs(r, c):
            acc = 0 
            visited.add((r, c))
            for dr, dc in dirs:
                nc, nr = r + dr, c + dc

                if in_bounds(nc, nr) and (nc, nr) not in visited and grid[nc][nr] == 1 :
                    acc = max(acc, dfs(nc, nr))
            return 1 + acc

        for row in grid:
            print(row)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))
        return max_area
