import math
class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31
        MAX = -(MIN + 1)
        
        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x/10)

            if ((res > MAX // 10 or 
                (res == MAX // 10 and digit >= MAX % 10))
                    or
                (res < MIN // 10 or 
                (res == MIN // 10 and digit <= MIN % 10))
                ):
                return 0
            res = (res * 10) + digit
        return res
    

class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x>0:
            res = res * 10 + x % 10
            x //=10

        if sign * res < -2**31 or sign * res > 2**31 - 1:
            return 0
        return res * sign
    
class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = int(str(abs(x))[-1::-1])
        if (negative): x *= (-1)
        if (-2**31 <= x <= 2**31 - 1): return x
        return 0