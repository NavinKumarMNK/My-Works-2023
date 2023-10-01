from collections import defaultdict

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen, frequency, stack = set(), defaultdict(int), []
        for (i, char) in enumerate(s):
            frequency[char] += 1
        
        for (i, char) in enumerate(s):
            frequency[char] -= 1 
            if char not in seen:
                while stack and stack[-1] > char and frequency[stack[-1]] != 0:
                    seen.remove(stack.pop())
                    
                stack.append(char)
                seen.add(char)

        return ''.join(stack)

