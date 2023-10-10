class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        n = len(mat)
        for i in range(n):
            sum += mat[i][i]
            if i != n-1-i:
                sum += mat[i][n-i-1]

        return sum 
