from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        count = 0
        while True:
            try:
                nums.remove(val)
                count+=1 
            except Exception as e:
                print(e)
                break
        
        return n - count 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
