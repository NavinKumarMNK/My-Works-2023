class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_count = left = right = 0
        for i in range(len(s)):
            if s[i] == '(' : left+=1
            elif s[i] == ')' : right+=1
            if left == right : 
                max_count = max(2*left, max_count) 
            elif left - right < 0:
                left = right = 0 

        left = right = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '(' : left+=1
            elif s[i] == ')' : right+=1
            if left == right : 
                max_count = max(2*right, max_count) 
            elif right - left < 0:
                left = right = 0 

        return max_count


                