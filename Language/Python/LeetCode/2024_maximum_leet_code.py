import collections

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def check(char):
            print(char)
            left = max_rept = wrong = 0
            positions = []
            for pos, right in enumerate(answerKey):
                if right != char:
                    wrong+=1
                    positions.append(pos)
                    if wrong == k+1:
                        max_rept = max(max_rept, pos-left)
                        left = positions.pop(0)+1
                        wrong-=1

            max_rept = max(max_rept, pos-left+1)

            return max_rept

        a, b = check('T'), check('F')
        print(a, b)
        return max(a, b)
    

class Solution:
    def maxConsecutiveAnswers(self, answerKey, k):
        max_freq = i = 0
        char_count = collections.Counter()

        for j in range(len(answerKey)):

            char_count[answerKey[j]] += 1
            max_freq = max(max_freq, char_count[answerKey[j]])

            if j - i + 1 > max_freq + k:
                char_count[answerKey[i]] -= 1
                i += 1

        return len(answerKey) - i