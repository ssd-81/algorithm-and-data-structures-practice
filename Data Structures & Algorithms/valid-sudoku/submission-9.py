class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        cols_set = [set() for _ in range(COLS)]
        rows_set = [set() for _ in range(ROWS)]
        grid_set = [[set() for _ in range(ROWS//3)] for _ in range(COLS//3)]

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rows_set[r] or val in cols_set[c] or val in grid_set[r//3][c//3]:
                    return False
                rows_set[r].add(val)
                cols_set[c].add(val)
                grid_set[r//3][c//3].add(val)
        return True 
