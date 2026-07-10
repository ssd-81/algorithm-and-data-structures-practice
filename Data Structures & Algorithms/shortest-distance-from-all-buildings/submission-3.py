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
        if len(destination) >= (len(grid) * len(grid[0])):
            return -1

        def in_bound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def breath_first_search(r, c):
            total_cost = 0 
            visited = set()
            visited.add((r,c))
            queue = deque([(r, c, 0)])

            while queue:
                qLen = len(queue)

                for i in range(qLen):
                    rx, cx, dis = queue.popleft()
                    if (rx,cx) in destination:
                        total_cost += dis
                        continue 
                    for dr, dc in dirs:
                        if in_bound(rx + dr, cx + dc) and  grid[rx+dr][cx+dc] not in block and (rx + dr, cx + dc) not in visited:
                            queue.append((rx + dr, cx + dc, dis + 1))
                            visited.add((rx + dr, cx + dc))
            return total_cost if total_cost else -1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in destination and (r,c) not in block:
                    grid_call = breath_first_search(r,c)
                    cost = min(cost, grid_call) 

        return cost 
                        