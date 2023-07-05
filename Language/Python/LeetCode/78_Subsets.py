from functools import cache
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets =[()]
        
        @cache
        def recursion(array, i):
            print(array, i)
            if len(array) == 0:
                return tuple([])
            elif i >= len(array):
                return tuple(array)
            
            array2 = list(array)
            del array2[i]
            ele1 = recursion(tuple(array2), i)
            ele2 = recursion(tuple(array), i+1)
            subsets.append(ele1)
            subsets.append(ele2)
            
            return tuple(array)
        
        recursion(tuple(nums), 0)
        return list(set(subsets))


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        def solve(i):
            if i == len(nums) : ans.append(subset.copy())
            else :
                subset.append(nums[i])
                solve(i+1)

                subset.pop()
                solve(i+1)

        solve(0)
        return ans