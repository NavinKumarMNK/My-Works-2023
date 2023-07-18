class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = triangle[-1].copy()
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = triangle[i][j] + min(res[j], res[j+1])

        print(res)
        return res[0]
