class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * (len(nums))
        prod_left, prod_right = 1, 1
        for pos in range(0, len(nums)-1):
            prod_left, prod_right = prod_left*nums[pos], prod_right*nums[~pos]
            output[pos+1] = prod_left*output[pos+1]
            output[~(pos+1)] = prod_right*output[~(pos+1)]
        return output
