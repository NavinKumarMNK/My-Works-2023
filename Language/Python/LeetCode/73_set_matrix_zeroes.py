class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_zero = False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        row_zero = True

        for r in range(1, m):
            for c in range(1, n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(m):
                matrix[r][0] = 0

        if row_zero:
            for c in range(n):
                matrix[0][c] = 0
