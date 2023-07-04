class Solution:
    def hammingWeight(self, num: int) -> int:
        """
        num & 1 = x if x is one then count+=1 , num >> 1
        count = 0
        while num:
            count += num & 1
            num = num >> 1

        """
        count = 0
        while num:
            num = num & (num -1)
            count += 1


        return count 