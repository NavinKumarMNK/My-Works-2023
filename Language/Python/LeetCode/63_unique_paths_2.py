class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: List[List[int]]) -> int:
        row = [0] * (len(obstacle_grid[0])+1)
        m, n = len(obstacle_grid), len(obstacle_grid[0])
        row[n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacle_grid[i][j]:
                    row[j] = 0
                else:
                    row[j] = row[j+1] + row[j]

        return row[0]
