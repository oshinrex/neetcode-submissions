class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose 
        for r in range(len(matrix)):
            for c in range(r+1, len(matrix)):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # reverse 
        for r in range(len(matrix)): 
            for c in range(len(matrix) // 2): 
                matrix[r][c], matrix[r][len(matrix) - c - 1] = matrix[r][len(matrix) - c - 1], matrix[r][c]