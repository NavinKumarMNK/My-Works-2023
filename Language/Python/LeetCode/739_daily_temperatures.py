from typing import List
from collections import Deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = Deque()  # [ele, pos]
        last = -1
        for pos, i in enumerate(temperatures):
            while stack and stack[-1][0] < i:
                ele = stack.pop()
                temperatures[ele[1]] = pos - ele[1]
            stack.append([i, pos])

        while stack:
            a, b = stack.pop()
            temperatures[b] = 0

        return temperatures
