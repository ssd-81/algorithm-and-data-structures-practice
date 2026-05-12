class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        RowSet = [set() for _ in range(ROWS)]
        ColSet = [set() for _ in range(COLS)]
        GridSet = [[set() for _ in range(ROWS//3)] for _ in range(COLS//3)]

        
        for r in range(ROWS):
            for c in range(COLS):
                curr = board[r][c]
                if curr == ".":
                    continue 
                if curr in RowSet[r] or curr in ColSet[c] or curr in GridSet[r//3][c//3]:
                    return False
                RowSet[r].add(curr)
                ColSet[c].add(curr)
                GridSet[r//3][c//3].add(curr)

        return True