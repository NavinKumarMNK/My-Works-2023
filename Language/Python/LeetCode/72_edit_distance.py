class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[0] * (len(word2)+1) for i in range(len(word1)+1)]
        
        for i in range(len(word1)):
            cache[i][0] = i
        for j in range(len(word2)):
            cache[0][j] = j
        
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    cache[i][j] = cache[i-1][j-1]
                else:
                    cache[i][j] = 1 + min(
                        cache[i-1][j], # delete
                        cache[i][j-1], # add
                        cache[i-1][j-1] # replace
                    )

        return cache[len(word1)][len(word2)]
    
# bottom up
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[float("infinity")] * (len(word2)+1) for i in range(len(word1)+1)]
        for j in range(len(word2)+1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1)+1):
            cache[i][len(word2)] = len(word1) - i
        
        for i in range(len(word1) -1, -1, -1):
            for j in range(len(word2) -1, -1, -1):
                if word1[i] == word2[j]: cache[i][j] = cache[i+1][j+1]
                else: cache[i][j] = min(cache[i+1][j+1], # replace
                                        cache[i+1][j], # delete
                                        cache[i][j+1] # add
                                    ) + 1
        
        return cache[0][0]
