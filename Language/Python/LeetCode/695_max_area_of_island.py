class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_count = 0

        def dfs(i, j):
            if i >= m or j >= n or i < 0 or j < 0:
                return 0

            if grid[i][j] != 1:
                return 0

            grid[i][j] = -1
            return dfs(i-1, j) + dfs(i, j-1) + dfs(i+1, j) + dfs(i, j+1) + 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_count = max(max_count, dfs(i, j))

        return max_count
