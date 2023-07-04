# not valid for negative numbers
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            x = a ^ b
            b = (a & b) << 1
            a = x
        return a
        
class Solution:
    def getSum(self, a: int, b: int) -> int:
        f=0
        if a<0 and b<0:
            f=1
        mask=0xffffffff
        add=a^b
        carry=(a&b)<<1
        while carry!=0:
            add,carry=(add^carry)&mask,((add&carry)<<1)&mask
        if f:
            return ~(add^mask)
        return add       