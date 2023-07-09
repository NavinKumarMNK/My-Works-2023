import heapq
from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        while k > 0:
            ele = -heapq.heappop(nums)
            k-=1

        return ele

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(l,r):
            index = random.randint(l, r)
            pivot = nums[index]
            nums[r], nums[index] = pivot, nums[r]
            storeIndex = l
            for i in range(l, r):
                if nums[i] > pivot:
                    nums[storeIndex], nums[i] = nums[i], nums[storeIndex]
                    storeIndex+=1
            
            nums[storeIndex], nums[r] = nums[r], nums[storeIndex]
            return storeIndex

        def quick_select(l, r, k):
            if l < r:
                index = partition(l, r)
                if index < k: quick_select(index+1, r, k)
                elif index > k: quick_select(l, index-1, k)
                else: return
                
        quick_select(0, len(nums)-1, k-1)
        print(nums)
        return nums[k-1]
