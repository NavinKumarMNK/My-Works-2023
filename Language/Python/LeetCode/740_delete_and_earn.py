class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        (nums := list(count.keys())).sort()
        earn1, earn2 = 0, 0  # second previous, previous
        for i in range(len(nums)):
            if nums[i] == nums[i-1] + 1:
                earn1, earn2 = earn2, max(
                    earn2, (nums[i] * count[nums[i]]) + earn1)
            else:
                earn1, earn2 = earn2, (nums[i] * count[nums[i]]) + earn2

        return earn2
