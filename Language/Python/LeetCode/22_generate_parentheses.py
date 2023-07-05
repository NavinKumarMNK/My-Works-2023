from functools import cache
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        @cache
        def solve(str, char, i, j):
            if j>i:
                return
            if i > n or j > n:
                return 
            
            a = solve(str+'(', '(', i+1, j)
            b = solve(str+')', ')', i, j+1)
            print(str, char, i, j, a, b)

            if a is not None and len(a) == 2*n:
                ans.append(a)
            if b is not None and len(b) == 2*n:
                ans.append(b)
            return str

        solve("(", "",  1, 0)
        return ans
    

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left, right, s):
            if right == n: res.append(s)
            else:
                if left < n: dfs(left + 1, right, s + "(")
                if right < left: dfs(left, right + 1, s + ")")
        
        dfs(0,0,"")
        return res