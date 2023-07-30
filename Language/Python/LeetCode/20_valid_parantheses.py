class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        _open = ['(', '[', '{']
        _close = [')', ']', '}']
        for char in s:
            if char in _open:
                stack.append(char)
            if char in _close:
                if len(stack) == 0:
                    return False
                a = stack.pop()
                idx = _open.index(a)
                b = _close[idx]
                if char != b:
                    return False

        return True if len(stack) == 0 else False


class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
