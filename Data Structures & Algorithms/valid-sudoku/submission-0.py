class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        column = set()
        for i in range(len(board)):
            # row = set()
            for j in range(len(board[i])):
                if board[i][j] in row:
                    return False
                if board[i][j] is not ".":
                    row.add(board[i][j])

                # column
                if board[j][i] in column:
                    return False
                if board[j][i] is not ".":
                    column.add(board[j][i])
            row = set()
            column = set()
        
        return True

            
        