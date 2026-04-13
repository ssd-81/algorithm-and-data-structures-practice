class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid) , len(grid[0])
        visited = set()
        
         
        def bfs(r, c):
            if grid[r][c] == 1:
                return -1
            q = deque()
            visited.add((r,c))
            q.append((r,c, 0))

            directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (1 , -1), (-1, -1)]

            while q:
                r, c, p = q.popleft() # row, col, path len so far
                if r == ROWS - 1 and c == COLS - 1:
                    p += 1
                    return p
                
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if 0<=newR<ROWS and 0 <= newC < COLS and grid[newR][newC] == 0 and (newR, newC) not in visited:
                        q.append((newR, newC, p + 1))
                        visited.add((newR, newC))
            return -1


        return(bfs(0, 0))
        


                
