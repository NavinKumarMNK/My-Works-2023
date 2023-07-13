INT_MAX = 2147483648
class MinStack:
    def __init__(self):
        self.stack = Deque()
        self.min = INT_MAX

    def push(self, val: int) -> None:
        if val < self.min: self.min = val
        self.stack.append((val, self.min))

    def pop(self) -> None:
        element = self.stack.pop()
        if element[0] == element[1]: 
            if self.stack:
                self.min = self.stack[-1][1]
            else:
                self.min = INT_MAX

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()