class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        i = 0
        
        while length < k:
            if s[i].isdigit():
                length *= int(s[i])
            else:
                length += 1
            i += 1
        
        for j in range(i-1, -1, -1):
            char = s[j]
            if char.isdigit():
                length //= int(char)
                k %= length
            else:
                if k == 0 or k == length:
                    return char
                length -= 1

class Solution:
    def decodeAtIndex(self, string: str, k: int) -> str:
        temp = ""
        last = 0
        for (i, s) in enumerate(string):
            if s.isdigit():
                num = int(string[i])
                temp += string[last:i]
                last=i+1
                if len(temp)*num >= k:
                    return temp[(k%len(temp))-1]
                temp*=num

        #print(temp, string)       
        return string[k-1]
