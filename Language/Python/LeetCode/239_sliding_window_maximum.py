class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, res = deque(), []
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if r+1 < k: continue
            if q[0] < r+1-k:
                q.popleft()
            res.append(nums[q[0]])

        return res