class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        ans = [''] * numRows
        index = 0
        for char in s:
            ans[index] += char
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1

            index += step

        return ''.join(ans)
