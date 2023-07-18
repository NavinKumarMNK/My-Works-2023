class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            for [l, r] in [[i, i], [i, i+1]]:
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    count += 1
                    l, r = l-1, r+1

        return count
