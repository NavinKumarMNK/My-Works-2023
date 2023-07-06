from typing import List

class Solution:
    def canPlace(self, chess: List[List[str]], i, j) -> bool:
        print("entry", i, j)
        if i==0: return True
        for x in range(len(chess)):
            if i==1:
                print("loop", x, chess)
            if chess[x][j] == 'Q':
                return False
            if chess[i][x] == 'Q':
                return False
                        
            if (j-i+x >= 0 and j-i+x < len(chess)) and chess[x][j-i+x] == 'Q':
                if i==0:
                    print(chess[x][j-i+x], x, j-i+x)
                return False
        
            if (j+i-x >= 0 and j+i-x < len(chess)) and chess[x][j+i-x] == 'Q':
                if i==0:
                    print(chess[x][j+i-x], x, j+i-x)
                return False
        
        return True              

    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions=[]
        chess = [["." for _ in range(n)] for _ in range(n)]
        
        def nqueens(chess, i):
            for j in range(len(chess)):
                if(self.canPlace(chess, i, j)) == True:
                    chess[i][j] = 'Q'
                    print(chess, True)
                    if i == len(chess)-1 :
                        temp = chess.copy()
                        for i in range(n):
                            chess[i] = "".join(chess[i])
                        print("Answer", chess)
                        solutions.append(chess.copy())
                        print("Answer", chess)
                        chess = temp
                        chess[i][j] = '.'
                        return
                else: continue 
                nqueens(chess.copy(), i+1)
                chess[i][j] = '.' 

            
        nqueens(chess, 0)
        print(solutions)

        return solutions
    
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if (r == n):
                res.append(["".join(row) for row in board])
                return
            

            for c in range(n):
                if ( c in col or (r + c) in posDiag or (r - c) in negDiag ):
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                
                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)

        return res