class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        hash_map = {}
        max_length = 0

        for n in arr:
            hash_map[n] = x = 1+hash_map.get(n-difference, 0)
            max_length = max(max_length, x)

        return max_length
