from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        positions = defaultdict(int)
        start = 0
        for i, ch in enumerate(s):
            start = max(start, positions[ch])
            count = max(count, i-start+1)
            positions[ch] = i + 1
        return count 
    
print(Solution.lengthOfLongestSubstring(Solution, "abcabcbb"))