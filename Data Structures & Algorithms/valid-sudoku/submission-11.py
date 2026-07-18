class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(len(board))]
        col_set = [set() for _ in range(len(board[0]))]
        grid_set = [[set() for _ in range(len(board[0])//3)] for _ in range(len(board)//3)] # not sure about this dimension


        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val == ".":
                    continue 
                if val in row_set[r] or val in col_set[c] or val in grid_set[r//3][c//3]:
                    return False
                row_set[r].add(val)
                col_set[c].add(val)
                grid_set[r//3][c//3].add(val)
        
        return True 
