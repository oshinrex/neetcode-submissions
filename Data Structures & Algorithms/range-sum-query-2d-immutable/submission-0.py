class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.sum_matrix = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        for i in range(1, len(self.sum_matrix)):
            for j in range(1, len(self.sum_matrix[0])):
                self.sum_matrix[i][j] = self.sum_matrix[i - 1][j] + self.sum_matrix[i][j - 1] + matrix[i - 1][j - 1] - self.sum_matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum_matrix[row2 + 1][col2 + 1] - self.sum_matrix[row1][col2 + 1] - self.sum_matrix[row2 + 1][col1] + self.sum_matrix[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)