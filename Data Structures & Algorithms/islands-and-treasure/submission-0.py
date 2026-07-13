class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]


        def in_bounds(r, c):
            return 0 <= r < rows and 0 <= c < cols

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        dist = 0 
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist 
                
                for dr, dc in dirs:
                    if in_bounds(r + dr, c + dc) and grid[r+dr][c+dc] != -1 and (r+dr, c+dc) not in visit:
                        q.append((r+dr, c+dc))
                        visit.add((r+dr, c+dc)) # should it be here or somewhere else 
            dist += 1
        