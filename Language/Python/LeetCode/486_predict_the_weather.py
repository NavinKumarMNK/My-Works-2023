class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        @cache
        def score(left, right):
            if left > right:
                return 0
            if left == right:
                return nums[left]

            left_score = nums[left] - score(left+1, right)
            right_score = nums[right] - score(left, right-1)

            return max(left_score, right_score)

        return score(0, len(nums)-1) >= 0
