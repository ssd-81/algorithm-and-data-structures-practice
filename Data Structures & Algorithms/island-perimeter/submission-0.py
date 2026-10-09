class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        # once a cell is found we start calculating the perimeter 
        def in_range(r, c):
            return  0 <= r < len(grid) and 0 <= c < len(grid[0])

        dirs = [(0,1), (1, 0), (0, -1), (-1, 0)]
        def calc_perimeter(r, c):
            visited = set()
            perimeter = 0 
            queue = deque([(r,c)])
            while queue:
                r_, c_ = queue.popleft()
                visited.add((r_, c_))
                cover = 0
                for dir in dirs:
                    if in_range(r_+ dir[0], c_ + dir[1]) and grid[r_ + dir[0]][c_ + dir[1]] == 1:
                        cover += 1
                        if (r_ + dir[0], c_ + dir[1]) not in visited:
                            queue.append((r_ + dir[0], c_ + dir[1]))
                perimeter += 4 - cover
            return perimeter 

        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if grid[r][c] == 1:
                    perimeter = calc_perimeter(r,c)
                    return perimeter
                