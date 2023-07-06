from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def backtrack(arr, i):
            if arr in permutations: return 
            permutations.append(arr.copy())
            for n in range(i, len(arr)):
                arr[i], arr[n] = arr[n], arr[i]
                backtrack(arr, i)
                arr[i], arr[n] = arr[n], arr[i]

        backtrack(nums, 0)
        return permutations 
