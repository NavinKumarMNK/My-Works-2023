class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        params = [] # [start, end, pos, count]
        last = count = 0
        pos = 0
        
        for i in range(len(nums)):
            if nums[i] < 0:
                count+=1
            if nums[i] == 0:
                if nums[last:i] != []:
                    params.append([last, i, pos, count])
                    count = 0
                    pos += 1
                
                last = i+1
                    

        if nums[last:] != []:
            params.append([last, len(nums), pos, count])
        
        # print(params)

        max_len = 0
        for i in params:
            if i[3] % 2 == 0:
                max_len = max(max_len, i[1]-i[0])
            else:
                k, l = i[0], i[1] - 1
                while k<l:
                    if nums[k] < 0 :
                        max_len = max(max_len, i[1] -1 - k)
                        break
                    if nums[l] < 0 :
                        max_len = max(max_len, l-i[0])
                        break
                    k+=1
                    l-=1

        return max_len
