class Solution:
    def decodeString(self, s: str) -> str:
        stack = Deque()
        result = ''
        digit = ''
        for n in s:
            print(stack)
            if n.isdigit():
                digit+=n
                continue
            elif digit and digit.isdigit():
                stack.append(int(digit))
                digit = ''
            if n=="]":
                sub = ''
                while (t:=stack.pop()) != '[': 
                    sub=sub+t[::-1]
                print(sub)
                num = stack.pop()
                sub = sub[::-1]*num  
                stack.append(sub)
            else:
                stack.append(n)

        result = ''.join(stack)
        return result