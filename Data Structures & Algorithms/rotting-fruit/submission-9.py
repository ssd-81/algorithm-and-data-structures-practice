class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def in_bounds(r, c):
            return 0 <= r <  ROWS and 0 <= c < COLS

        sources = deque()
        fresh_fruits = 0 

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    sources.append((r, c))
                elif grid[r][c] == 1:
                    fresh_fruits += 1
        
        dirs = [(-1,0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        time = 0 

        while sources:
            qLen = len(sources)
            for i in range(qLen):
                r, c = sources.popleft()

                for dr, dc in dirs:
                    if (r+dr, c+dc) not in visited and in_bounds(r + dr, c + dc) and grid[r+dr][c+dc] == 1:
                        sources.append((r+dr, c+dc))
                        visited.add((r+dr, c+dc))
                        fresh_fruits -=1
            time += 1
        return time-1 if fresh_fruits == 0 else -1



