class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in row[i] or board[i][j] in column[j] or board[i][j] in boxes[(i//3, j//3)] :
                    
                    return False

                # if board[i][j] != ".":
                row[i].add(board[i][j])

                # if board[j][i] != ".":
                column[j].add(board[i][j])

                # if board[i][j] != ".":
                    # check_set.add(board[i][j])
                boxes[(i//3, j//3)] = boxes[(i//3, j//3)].add(board[i][j])

            row = set()
            column = set()
        
        return True

            
        