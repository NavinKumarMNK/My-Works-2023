class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def recursive(tot):
            if tot > target:
                return 0
            if tot == target:
                return 1

            calc = 0
            for i in nums:
                calc += recursive(tot+i)

            return calc

        res = recursive(0)
        print(res)
        return res


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {0: 1}
        for total in range(1, target+1):
            cache[total] = 0
            for n in nums:
                cache[total] += cache.get(total-n, 0)

        return cache[target]
