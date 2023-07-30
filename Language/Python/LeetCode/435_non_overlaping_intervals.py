class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = i = 0
        while i < len(intervals):
            a, b = intervals[i]
            j = i+1
            while j < len(intervals) and b > intervals[j][0]:
                count += 1
                x, y = intervals[j]
                b = min(b, y)
                j += 1
            i = j

        return count
