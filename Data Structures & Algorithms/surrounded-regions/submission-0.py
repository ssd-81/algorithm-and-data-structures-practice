class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])


        # inversion thinking 

        def capture(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return 
            
            board[r][c] = 'T'
            capture(r + 1, c)
            capture(r - 1, c)

