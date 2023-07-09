import heapq
import math
from typing import List
import random

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        for x, y in points:
            dist= x**2 + y**2
            minHeap.append((dist, (x, y)))
        
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            res.append(heapq.heappop(minHeap)[1])
            k-=1 
        
        return res

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def partition(l, r):
            index = random.randint(l, r)
            pivot = distances[index][0]
            distances[index], distances[r] = distances[r], distances[index]
            storeIndex = l
            for i in range(l, r):
                if distances[i][0] < pivot:
                    distances[storeIndex], distances[i] = distances[i], distances[storeIndex]
                    storeIndex += 1
            
            distances[storeIndex], distances[r] = distances[r], distances[storeIndex]
            return storeIndex
            
        def quickselect(l, r, k):
            if l < r:
                pindex = partition(l, r)
                if pindex == k:
                    return 
                elif pindex < k:
                    quickselect(pindex+1, r, k)
                else:
                    quickselect(l,pindex-1, k)

        distances = [(x**2 + y**2, (x,y)) for x,y in points]
        quickselect(0, len(distances)-1, k)
        return [coord for _, coord in distances[:k]]