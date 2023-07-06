from functools import cache
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []

        @cache
        def backtrack(strings):
            false = False
            if len(strings) == len(s): 
                results.append(strings)
                return None
            
            for string in strings:

                print("Main", string)
                if string != string[::-1]:
                    false = True

                for i in range(1, len(string)):
                    ret_strings = list(strings)
                    ind = ret_strings.index(string)
                    ret_strings.remove(string)
                    ret_strings.insert(ind, string[:i])
                    ret_strings.insert(ind+1, string[i:])
                    a = backtrack(tuple(ret_strings))

            if false == False:
                results.append(strings)


            return string  

        backtrack(tuple([s]))
        return results
    
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)  
        dp = [[] for i in range(n+1)] 
        dp[-1].append([]) 
        for i in range(n-1,-1,-1):
            for j in range(i+1,n+1):
                curr = s[i:j] 
                if curr == curr[::-1]:  
                    for e in dp[j]:   
                        dp[i].append ([curr] + e)
        return dp[0]      
		