from functools import cache
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        non_obstacles = sum(cell != -1 for row in grid for cell in row)

        (i, j) = next((i, j) for i in range(m)
                      for j in range(n) if grid[i][j] == 1)

        def dfs(i, j, steps):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0

            if grid[i][j] == 2:

                return steps == non_obstacles

            if grid[i][j] == -1:
                return 0

            temp = grid[i][j]
            grid[i][j] = -1
            count = dfs(i+1, j, steps+1) + dfs(i, j+1, steps+1) + \
                dfs(i-1, j, steps+1) + dfs(i, j-1, steps+1)
            grid[i][j] = temp

            return count

        return dfs(i, j, 1)
