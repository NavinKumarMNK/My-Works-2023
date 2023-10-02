class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count_a = count_b = 0
        temp, flag = 0, 0 # flag => 0 - A, 1 - B
        for i in colors:
            if i == 'A':
                if flag == 1:
                    flag, temp = 0, 0
                temp += 1
                count_a = count_a + 1 if temp >= 3 else count_a
                
            elif i == 'B':
                if flag == 0:
                    flag, temp = 1, 0
                temp += 1
                count_b = count_b + 1 if temp >= 3 else count_b
                
        return True if count_a > count_b else False
