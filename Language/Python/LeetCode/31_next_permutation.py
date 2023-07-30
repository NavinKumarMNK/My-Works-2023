class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        pos = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                pos = i
                break

        if pos == -1:
            nums.reverse()
            return None

        for i in range(len(nums)-1, pos, -1):
            if nums[i] > nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
                break

        nums[pos+1:] = nums[pos+1:][::-1]

        return None
