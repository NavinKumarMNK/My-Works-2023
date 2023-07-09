from typing import List
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        new_arr = []
        for i in range(len(weights)-1):
            sump = weights[i] + weights[i+1]
            new_arr.append((sump, i))
        
        new_arr.sort(key=lambda x: x[0])

        inc = []
        for i in range(k-1):
            inc.append(new_arr[i][1])
        
        dec = []
        for i in range(k-1):
            dec.append(new_arr[len(new_arr)-1-i][1])
        
        dec.sort()
        inc.sort()

        max_sum = min_sum = weights[0] + weights[len(weights)-1]
        for i in range(len(weights)):
            if len(inc) > 0 and i == inc[0]:
                min_sum+=weights[i] + weights[i+1]
                inc.pop(0)
            if len(dec) > 0 and i == dec[0]:
                max_sum+=weights[i] + weights[i+1]
                dec.pop(0)
        
        return max_sum - min_sum
    

class Solution:
    def putMarbles(self, w: List[int], k: int) -> int:
        p = sorted([w[i] + w[i + 1] for i in range(len(w) - 1)])
        return sum(p[len(p) - k + 1:]) - sum(p[:k - 1])