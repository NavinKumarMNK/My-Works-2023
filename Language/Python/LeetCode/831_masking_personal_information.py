class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            ind = s.find('@')
            s = s[0] + '*****' + s[ind-1:]
        else:    
            for x in '+-() ':
                s = s.replace(x, '')

            ln = len(s)
            res = ''
            if ln>10:
                res = '+'+'*'*(ln-10)+'-'
            res+='***-***-'+s[-4:]
            s = res
        return s


