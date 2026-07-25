class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0 
        visited = set()
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def in_bound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def bfs(root):
            queue = deque([root])
            island_size = 0

            while queue:
                r, c = queue.popleft()
                island_size += 1
                visited.add((r, c))

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if in_bound(nr, nc) and (nr, nc) not in queue and (nr,nc) not in visited and grid[nr][nc] == 1:
                        queue.append((nr, nc))
            return island_size 
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    print("call was made: ", r ,c )
                    cur = bfs((r,c))
                    print(cur)
                    maxArea = max(maxArea, cur)

        return maxArea 