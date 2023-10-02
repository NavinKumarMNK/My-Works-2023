class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        land, border = 0, 0

        def dfs(i, j):
            nonlocal border
            visited.add((i, j))
            for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                x = i+x
                y = j+y
                if not (x < 0 or y < 0 or x > n-1 or y > m-1):
                    if grid[x][y] == 1 and (x, y) not in visited:
                        border+=1 
                        dfs(x, y)
                
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    land+=1
                    if (i, j) not in visited and  \
                        (i == 0 or j == 0 or i == n-1 or j == m-1):
                        border+=1
                        dfs(i, j)
        
        return land - border

