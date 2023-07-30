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


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = res = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])
            res = max(res, r-l+1)

        return res


print(Solution.lengthOfLongestSubstring(Solution, "abcabcbb"))
