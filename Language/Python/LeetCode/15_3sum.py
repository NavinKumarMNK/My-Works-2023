class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        nums.sort()

        for pos, i in enumerate(nums[:-1]):
            left, right = pos+1, len(nums)-1
            if i > 0:
                break
            while left < right:
                if nums[left] + nums[right] + i == 0:
                    results.add((i, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] + i < 0:
                    left += 1
                else:
                    right -= 1

        return results

        # [-1, -1, 0, 1, 2, 4]
