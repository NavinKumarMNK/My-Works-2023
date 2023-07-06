from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        boolean = False
        visited = [[False] * n for _ in range(m)]

        def dfs(i, j, index):
            nonlocal boolean
            if index == len(word):
                boolean = True
                return

            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or board[i][j] != word[index]:
                return

            visited[i][j] = True
            dfs(i + 1, j, index + 1)
            dfs(i - 1, j, index + 1)
            dfs(i, j + 1, index + 1)
            dfs(i, j - 1, index + 1)
            visited[i][j] = False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    dfs(i, j, 0)
                    if boolean:
                        return True

        return boolean
    

import copy
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        boolean = False
        
        def dfs(i, j, word):
            #print(word)
            nonlocal boolean
            visited[i][j] = -1
            if len(word) == 0:
                boolean = True
                return

            nears = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for near in nears:
                x, y = [x + y for x, y in zip(near, [i, j]) ]
                if x >= 0 and x <m and y >= 0 and y<n and visited[x][y]!=-1 and word[0]==board[x][y]:
                    if len(word) == 1: 
                        boolean=True 
                        return
                    print(x, y, word)
                    dfs(x, y, word[1:]) 
            
            visited[i][j] = 0

        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = copy.deepcopy(board)
                    print("here", i, j, board)
                    dfs(i, j, word[1:])
                
        return boolean