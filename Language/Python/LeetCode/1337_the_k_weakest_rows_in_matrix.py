from typing import List
import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        index = []
        m, n = len(mat), len(mat[0])
        count = []

        for i in range(m):
            temp = 0
            for j in range(0, n):
                temp += 1 
                if mat[i][j] == 0:
                    temp-=1
                    break
            count.append((temp, i)) # (count, pos)
        
        count.sort(key=lambda x: x[0])
        print(count)
        return [count[x][1] for x in range(k)] 


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_strength = [(sum(row), i) for i, row in enumerate(mat)]
        row_strength.sort(key=lambda x: (x[0], x[1]))
        return [row[1] for row in row_strength[:k]]

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def binarySearch(arr):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == 1:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        queue = [(binarySearch(row), idx) for idx, row in enumerate(mat)]
        heapq.heapify(queue)

        return [idx for _, idx in heapq.nsmallest(k, queue)]
