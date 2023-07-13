class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        _open = ['(', '[', '{']
        _close = [')', ']', '}']
        for char in s:
            if char in _open:
                stack.append(char)
            if char in _close:
                if len(stack) == 0: return False
                a = stack.pop()
                idx = _open.index(a)
                b = _close[idx]
                if char != b:
                    return False
        
        return True if len(stack) == 0 else False
    

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {'(': ')', '{': '}', '[': ']'}
        
        for char in s:
            if char in bracket_map:
                stack.append(char)
            elif char in bracket_map.values():
                if not stack or bracket_map[stack.pop()] != char:
                    return False
        
        return not stack

        # print(bracs.keys(),bracs.values())