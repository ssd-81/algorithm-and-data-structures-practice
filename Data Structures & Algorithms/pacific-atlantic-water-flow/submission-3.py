class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        results = []

        def can_reach_both(r, c):
            visited = set()
            reached_pacific = False
            reached_atlantic = False

            def dfs(row, col):
                nonlocal reached_pacific, reached_atlantic
                if (row, col) in visited:
                    return
                visited.add((row, col))

                # Check ocean borders
                if row == 0 or col == 0:
                    reached_pacific = True
                if row == m - 1 or col == n - 1:
                    reached_atlantic = True

                # Early exit
                if reached_pacific and reached_atlantic:
                    return

                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        if heights[nr][nc] <= heights[row][col]:  # water flows down
                            dfs(nr, nc)

            dfs(r, c)
            return reached_pacific and reached_atlantic

        for r in range(m):
            for c in range(n):
                if can_reach_both(r, c):
                    results.append([r, c])

        return results