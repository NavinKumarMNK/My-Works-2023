from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_table = {}
        for n in s:
            print(n)
            if hash_table.get(n, 0) == 0:
                hash_table[n]=0 
            hash_table[n]+=1 
        
        all_chars = []
        chars = []
        for i in range(len(s)):
            hash_table[s[i]]-=1
            chars.append(s[i])
            if hash_table[s[i]] == 0:
                flag = 0
                temp = set(chars)
                for i in temp:
                    if hash_table[i] != 0:
                        flag = 1
                        break
                if flag == 0 :
                    all_chars.append(len(chars))
                    chars = []
            
        return all_chars

        
