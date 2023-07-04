class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        i=31
        while n:
            c = n & 1
            n = n >> 1
            rev = rev | (c<<i)
            i-=1 
        
        return rev