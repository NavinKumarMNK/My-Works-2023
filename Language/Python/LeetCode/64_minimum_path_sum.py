from functools import cache
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def recursion(i, j):
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[i][j]

            a = b = float('inf')
            if i + 1 < len(grid):
                a = recursion(i + 1, j)
            if j + 1 < len(grid[0]):
                b = recursion(i, j + 1)

            return min(a, b) + grid[i][j]

        return recursion(0, 0)


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = [[float("inf")] * (cols + 1) for r in range(rows+1)]
        res[rows-1][cols] = 0
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r-1][c], res[r][c+1])
        
        return res[0][0]