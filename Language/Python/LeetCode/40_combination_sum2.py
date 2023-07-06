class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()

        def backtrack(remain, i, subset):
            if remain == 0 : results.append(subset.copy())
            if remain <= 0 or i >= len(candidates) : return None
 
            backtrack(remain-candidates[i], i+1, subset+[candidates[i]])
            while i+1 < len(candidates) and candidates[i+1] == candidates[i]: i+=1
            backtrack(remain, i+1, subset)
            

        backtrack(target, 0, [])
        return results
        
        