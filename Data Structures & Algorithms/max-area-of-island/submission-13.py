class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])

        
        visit = set()
        areas = []

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visit.add((r, c))

            area = 0
            while q:
                r, c = q.popleft()
                area += 1
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                        if (r + dr) in range(rows) and (c + dc) in range(cols) and grid[r+dr][c+dc] == 1 and (r+dr, c + dc) not in visit:
                            q.append((r + dr, c + dc))
                            visit.add((r + dr, c + dc))
            areas.append(area)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    bfs(r, c)       
        return max(areas) if len(areas) > 0 else 0



                    



