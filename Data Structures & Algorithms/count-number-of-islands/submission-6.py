class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        total_islands = 0 

        dirs = [(-1, 0), (1,0), (0, 1), (0,-1)]

        def dfs(r, c):
            visit.add((r,c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (nr>=0 and nc>=0 and nr < rows and nc < cols) and (nr,nc) not in visit and grid[nr][nc] == "1":
                    dfs(nr,nc)
            
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == "1":
                    dfs(r,c)
                    total_islands += 1
        return total_islands 