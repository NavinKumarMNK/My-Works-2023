class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        m = len(goal)
        if n != m:
            return False

        if s == goal:
            temp = set(s)
            if len(temp) < n:
                return True

        dct = {}
        count = 0
        for i in range(m):
            if s[i] != goal[i]:
                dct[s[i]] = goal[i]
                count += 1
        print(dct)

        if count == 2 and len(dct) == 2:
            lst = list(dct.keys())
            if dct[lst[0]] == lst[1] and dct[lst[1]] == lst[0]:
                return True
        else:
            return False


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        dic = [[a, b] for a, b in zip(s, goal) if a != b]
        return len(s) == len(goal) and (len(dic) == 2 and dic[0][0] == dic[1][1] and dic[1][0] == dic[0][1] or (len(dic) == 0 and len(set(s)) < len(goal)))
