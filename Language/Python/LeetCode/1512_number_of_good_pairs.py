class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        
        print(hash_map)

        count = 0
        nc2 = lambda n : n*(n-1)//2
        for i in hash_map.values():
            count += nc2(i)
        
        return count
                
            

