from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sn, tn = len(s), len(t)
        if tn > sn:
            return ""
        res = (0, float("inf"))
        need = defaultdict(int)

        for c in t:
            need[c] += 1
        l, missing = 0, len(t)

        for r, c in enumerate(s):
            if need[c] > 0:  # c is in t, 1 less char to match
                missing -= 1
            need[c] -= 1
            if missing > 0:
                continue

            while need[s[l]] < 0:  # remove preceding chars not needed
                need[s[l]] += 1
                l += 1
            if r - l < res[1] - res[0]:
                res = (l, r)

            need[s[l]] += 1  # remove the first char in window
            missing = 1
            l += 1
        return s[res[0]: res[1] + 1] if res[1] != float("inf") else ""


class Solution:
    def check(self, curMap, hashMap):
        for key in hashMap:
            if key not in curMap or curMap[key] < hashMap[key]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        hashMap = {}

        for i in range(len(t)):
            hashMap[t[i]] = 1 + hashMap.get(t[i], 0)

        left = right = 0
        curMap = {}
        ret_string = ""

        while right < len(s):
            while right < len(s) and not self.check(curMap, hashMap):
                if s[right] in hashMap:
                    curMap[s[right]] = 1 + curMap.get(s[right], 0)
                right += 1
            if self.check(curMap, hashMap):
                while left < len(s) and self.check(curMap, hashMap):
                    if s[left] in curMap:
                        curMap[s[left]] -= 1
                        if curMap[s[left]] == 0:
                            curMap.pop(s[left])
                    left += 1

                if ret_string == "":
                    ret_string = s[left-1:right]
                elif right-left+1 < len(ret_string):
                    ret_string = s[left-1:right]
            else:
                left += 1

        return ret_string


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashMap = {}

        for char in t:
            hashMap[char] = hashMap.get(char, 0) + 1

        left = right = 0
        ret_string = ""
        required_chars = len(t)

        while right < len(s):
            if s[right] in hashMap:
                hashMap[s[right]] -= 1
                if hashMap[s[right]] >= 0:
                    required_chars -= 1

            while required_chars == 0:
                if ret_string == "" or right - left + 1 < len(ret_string):
                    ret_string = s[left:right + 1]

                if s[left] in hashMap:
                    hashMap[s[left]] += 1
                    if hashMap[s[left]] > 0:
                        required_chars += 1

                left += 1

            right += 1

        return ret_string
