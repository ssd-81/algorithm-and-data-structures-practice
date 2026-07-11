class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        destination = set()
        block = set()
        cost = float('inf')
        dirs = [(0, 1), (0, -1), (1, 0), (-1,0)]
    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    destination.add((r, c))
                elif grid[r][c] == 2:
                    block.add((r, c))

        def in_bound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def breath_first_search(r, c):
            total_cost = 0 
            visited = set()
            visited.add((r,c))
            total_des = len(destination)
            queue = deque([(r, c, 0)])

            while queue and total_des != 0:
                qLen = len(queue)

                for i in range(qLen):
                    rx, cx, dis = queue.popleft()
                    if (rx,cx) in destination:
                        total_cost += dis
                        total_des -= 1
                        continue 
                    for dr, dc in dirs:
                        if in_bound(rx + dr, cx + dc) and  (rx + dr, cx + dc) not in block and (rx + dr, cx + dc) not in visited:
                            queue.append((rx + dr, cx + dc, dis + 1))
                            visited.add((rx + dr, cx + dc))
            if total_des != 0:
                for row in range(len(grid)):
                    for col in range(len(grid[0])):
                        if grid[row][col] == 0 and vis[row][col]:
                            grid[row][col] = 2
                return float('inf')

            return total_cost 

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in destination and (r,c) not in block:
                    grid_call = breath_first_search(r,c)
                    cost = min(cost, grid_call) 

        return cost if cost != float('inf') else -1 

                        