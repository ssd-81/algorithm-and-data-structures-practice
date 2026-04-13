class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        row_sets = [set() for _ in range(m)]
        col_sets = [set() for _ in range(n)]
        grid_sets = [[set() for _ in range(m)] for _ in range(n)]

        for i in range(m):
            for j in range(n):
                
                val = board[i][j]
                if val == ".":
                    continue
                if val in row_sets[i] or val in col_sets[j] or val in grid_sets[i//3][j//3]:
                    return False
                else:
                    row_sets[i].add(val)
                    col_sets[j].add(val)
                    grid_sets[i//3][j//3].add(val)
        return True