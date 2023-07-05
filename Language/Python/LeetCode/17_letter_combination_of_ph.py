from typing import List
from functools import cache

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dct = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", 's'],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"],
        }

        ans = []

        @cache
        def recursive(a, b, i, j):
            if i>=len(a) or j>=len(b):
                return 
            
            x = recursive(a, b, i, j+1)
            y = recursive(a, b, i+1, j)
            
            ans.append(a[i] + b[j])
            return a[i]+b[j]
        
        if len(digits) == 1:
            return dct[digits]

        for i in range(len(digits)-1):
            if i == 0: recursive(tuple(dct[digits[0]]), tuple(dct[digits[1]]), 0, 0)
            else:
                temp = ans[:]
                ans.clear() 
                recursive(tuple(temp), tuple(dct[digits[i+1]]), 0, 0)
            
        return ans

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        digits_to_char = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }

        def backtrack(i, cur):
            if len(cur) == len(digits):
                ans.append(cur)
                return
            for c in digits_to_char[digits[i]]:
                backtrack(i+1, cur+c)

        if digits:
            backtrack(0, "")
        
        return ans
