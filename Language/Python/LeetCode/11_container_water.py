class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            h1, h2 = height[left], height[right]
            max_area = max(max_area, min(h1, h2)*(right-left))
            if h1 < h2: left+=1
            else: right-=1

        return max_area