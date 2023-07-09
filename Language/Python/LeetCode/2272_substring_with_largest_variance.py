import itertools, collections

class Solution:
    def largestVariance(self, s: str) -> int:
        counter = collections.Counter(s)
        res = 0

        for char1, char2 in itertools.permutations(counter, 2):
            char1_count = counter[char1]
            char2_count = counter[char2]
            diff = 0

            seen_char1 = seen_char2 = False

            for char in s:
                if char not in (char1, char2): continue
                if diff < 0:
                    if not char1_count:
                        break

                    if not char2_count:
                        res = max(res, diff + char1_count)
                        break
                    
                    seen_char1 = seen_char2 = False
                    diff = 0
                
                if char == char1:
                    seen_char1 = True
                    char1_count-=1
                    diff+=1

                if char == char2:
                    seen_char2 = True
                    char2_count -=1
                    diff-=1

                if seen_char1 and seen_char2:
                    res = max(res, diff)

        return res  
