from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        n = [001, 001, 010, 001], ones = 000, twos = 000
        ones = 000 ^ 001 = (001) & ~000 = 001
        twos = 000 ^ 001 = (001) & ~001 = 000 # 001 is in ones so it should not be in twos

        ones = 001 ^ 001 = (000) & ~000 = 000 # 001 is in ones so it should not be in ones
        twos = 000 ^ 001 = (001) & ~000 = 001 # 001 is not in ones so it should be in twos

        ones = 000 ^ 010 = (010) & ~001 = 010 # 010 is not in ones so it should be in ones
        twos = 001 ^ 010 = (011) & ~010 = 001 # 010 is in ones so it should not be in twos

        ones = 010 ^ 001 = (011) & ~001 = 010 # 001 is in twos 
        twos = 001 ^ 001 = (000) & ~010 = 000 # 001 is in twos so it should not be in twos
        
        return 010
        """
        ones = twos = 0
        for n in nums:
            ones = (ones ^ n) & ~twos
            twos = (twos ^ n) & ~ones
            print(ones, twos)
        return ones

