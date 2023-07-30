from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix) < 1:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        max_val = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    if i > 0 and j > 0:
                        x = min(int(matrix[i-1][j-1]),
                                int(matrix[i-1][j]), int(matrix[i][j-1]))
                        matrix[i][j] = x + 1
                    max_val = max(max_val, int(matrix[i][j]))

        print(matrix)
        return max_val * max_val
