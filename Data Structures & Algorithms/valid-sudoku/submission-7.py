class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        row_sets = [set() for i in range(ROWS)]
        col_sets = [set() for i in range(COLS)]
        grid_set = [[set() for i in range(ROWS//3)] for j in range(COLS//3)]

        for i in range(ROWS):
            for j in range(COLS):
                val = board[i][j]
                if val == ".":
                    continue
                if val in row_sets[i] or val in col_sets[j] or val in grid_set[i//3][j//3]:
                    print(val)
                    print(row_sets)
                    print(col_sets)
                    print(grid_set)
                    return False
                else:
                    row_sets[i].add(val)
                    col_sets[j].add(val)
                    grid_set[i//3][j//3].add(val)
        return True