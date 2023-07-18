from typing import List
import collections


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        res = 0
        prefix = [0]
        stack = collections.deque()  # (pos, val)
        for i in nums:
            prefix.append(prefix[-1]+i)

        for i, n in enumerate(nums):
            new_start = i
            while stack and stack[-1][1] > n:
                start, val = stack.pop()
                total = prefix[i] - prefix[start]
                res = max(res, total*val)
                new_start = start

            stack.append((new_start, n))

        for start, val in stack:
            total = prefix[len(nums)] - prefix[start]
            res = max(res, total*val)

        return res % (10**9+7)


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        ans = 0
        stack = []
        # append "-inf" to force flush all elements
        for i, x in enumerate(nums + [-inf]):
            while stack and stack[-1][1] >= x:
                _, xx = stack.pop()
                ii = stack[-1][0] if stack else -1
                ans = max(ans, xx*(prefix[i] - prefix[ii+1]))
            stack.append((i, x))
        return ans % 1_000_000_007


class DisjointSet:
    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.parent_or_size = [-1]*n

    def union(self, a: int, b: int) -> int:
        x = self.find(a)
        y = self.find(b)

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x

        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x

        return x

    def find(self, a: int) -> int:
        parent = self.parent_or_size[a]
        while parent >= 0:
            if self.parent_or_size[parent] < 0:
                return parent
            self.parent_or_size[a], a, parent = (
                self.parent_or_size[parent],
                self.parent_or_size[parent],
                self.parent_or_size[self.parent_or_size[parent]]
            )

        return a

    def size(self, a: int) -> int:
        return -self.parent_or_size[self.leader(a)]


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:

        # we begin from the largest number to the smallest number
        nums = [0] + nums + [0]
        pos = [(x, i) for i, x in enumerate(nums)]
        pos.sort()
        pos.reverse()

        # we track the result with this variable
        maxres = 0

        # we track the membership of each element
        # d.find(x) == d.find(y) if x and y are in the same group
        d = DisjointSet(len(nums))

        # we track the current sum of each group with a dictionary
        # map group_id (which may change over time) to the sum
        segsums = {}

        # iterate from the largest to the smallest number and index
        # excluding the two zeros padded at the ends
        for x, i in pos[:-2]:
            minval = x  # current value is minimum since we iterate from large to small
            segsum = x

            # if the left element is larger
            if nums[i-1] > nums[i]:
                idx = d.find(i-1)       # get group index
                segsum += segsums[idx]  # include sum of adjacent group
                d.union(i, i-1)         # combine groups

            # equality because we iterate with decreasing index as well
            if nums[i+1] >= nums[i]:
                idx = d.find(i+1)
                segsum += segsums[idx]
                d.union(i, i+1)

            # update sum of group
            segsums[d.find(i)] = segsum

            # update the result
            maxres = max(maxres, minval*segsum)

        # remember to take modulo
        return maxres % (10**9+7)
