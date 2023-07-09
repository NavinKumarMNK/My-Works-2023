class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        results = []
        if numRows == 0 : return [[]] 
        for i in range(1, numRows+1):
            if i == 1: results.append([1])
            elif i == 2: results.append([1, 1])
            else: 
                lst = results[-1]
                temp = [1, 1]
                for j in range(1, i-1):
                    temp.insert(j, lst[j]+lst[j-1])
                results.append(temp)
        return results