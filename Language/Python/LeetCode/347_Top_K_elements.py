from typing import List
from heapq import *
from collections import Counter
 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = {}
        for i in nums:
            freq_table[i] = freq_table.get(i, 0) + 1
        heap = []
        for i in freq_table.keys():
            if len(heap) >= k: 
                heappushpop(heap, (freq_table[i], i))
            else: 
                heappush(heap, (freq_table[i], i))
		
        ans = []
        while k > 0:
            k -= 1
            ans.append(heappop(heap)[1])
        return ans
    
# Using Couter + most_common()    

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = Counter(nums)
        ans_table = freq_table.most_common()
        ans = []
        for key, _ in ans_table:
            if k <= 0:
                break
            k -= 1
            ans.append(key)
        return ans

#Using Counter + Heap + nlargest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = Counter(nums)
        heap = []
        for i in freq_table.keys():
            heappush(heap, (freq_table[i], i))
        freq_table = nlargest(k,heap)
        ans = []
        for i, j in freq_table:
            ans.append(j)
        return ans