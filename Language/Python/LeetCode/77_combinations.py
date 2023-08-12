from typing import List
import collections


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        arr = collections.deque()

        def backtracking(i):
            if i > n+1:
                return None

            if len(arr) == k:
                results.append(arr.copy())
                return None

            arr.append(i)
            backtracking(i+1)
            arr.pop()
            backtracking(i+1)

            return None

        backtracking(1)

        return results
