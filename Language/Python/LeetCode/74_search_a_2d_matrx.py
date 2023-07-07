class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m
        while low < high:
            mid = low + (high-low) // 2
            if matrix[mid][0] < target: low = mid + 1
            else: high = mid 

        print(low)
        if low < m and matrix[low][0] == target : return True 
        m = low-1 
        

        low, high = 0, n
        while low < high:
            mid = low + (high-low) // 2
            if matrix[m][mid] < target: low = mid + 1
            elif matrix[m][mid] > target : high = mid
            else: return True 

        print(low, mid, high)

        return False