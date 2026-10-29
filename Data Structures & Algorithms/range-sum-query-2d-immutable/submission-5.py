class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                self.prefix[r + 1][c + 1] = (matrix[r][c] 
                + self.prefix[r][c + 1] # top
                + self.prefix[r + 1][c] # left
                - self.prefix[r][c] # diagonal
                )
        # print(self.prefix)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = self.prefix[row2 + 1][col1]
        top = self.prefix[row1][col2 + 1]
        diagonal = self.prefix[row1][col1]
        res = self.prefix[row2 + 1][col2 + 1] - left - top + diagonal
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)