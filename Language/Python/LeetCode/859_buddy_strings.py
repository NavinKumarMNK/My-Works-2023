class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)
        m = len(goal)
        if n != m : 
            return False
        
        if s == goal:
            temp = set(s)
            if len(temp) < n:
                return True

        dct = {}
        count=0        
        for i in range(m):
            if s[i] != goal[i]:
                dct[s[i]] = goal[i]
                count+=1
        print(dct)

        if count == 2 and len(dct)==2:
            lst = list(dct.keys())
            if dct[lst[0]] == lst[1] and dct[lst[1]] == lst[0]:
                return True   
        else : return False
