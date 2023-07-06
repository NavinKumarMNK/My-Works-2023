class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        
        def solve(subset, i):
            subset = list(subset)
            subset.sort()
            if i == len(nums) :
                if subset not in ans:
                    ans.append(subset.copy())
            else :
                subset.append(nums[i])
                solve(tuple(subset), i+1)

                subset.pop()
                solve(tuple(subset), i+1)
            return None

        solve(tuple(subset), 0)
        return ans
    
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        nums.sort()
        def solve(subset, i):
            subset = list(subset)
            if i == len(nums) :
                ans.append(subset.copy())
            else :
                subset.append(nums[i])
                solve(list(subset), i+1)

                subset.pop()
                while i+1 < len(nums) and nums[i] == nums[i+1]:i+=1
                solve(list(subset), i+1)
            return None

        solve(tuple([]), 0)
        return ans


        