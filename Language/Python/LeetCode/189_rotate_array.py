class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:n-k] = nums[:n-k][::-1]
        nums[n-k:] = nums[n-k:][::-1]
        nums[:] = nums[::-1]
