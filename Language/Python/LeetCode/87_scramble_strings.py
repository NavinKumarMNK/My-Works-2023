class Solution:
    def __init__(self,):
        self.cache = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        # O(N)
        if len(s1) != len(s2):
            self.cache[(s1, s2)] = False
            return False

        # O(N)
        if len(s1) == 1:
            self.cache[(s1, s2)] = (s1 == s2)
            return s1 == s2

        # O(1)
        if (s1, s2) in self.cache:
            return self.cache[(s1, s2)]

        # O(N)
        if s1 == s2:
            self.cache[(s1, s2)] = True
            return True

        # Pruning: Frequency check # O(N)
        hash1, hash2 = {}, {}
        for i in range(len(s1)):
            hash1[s1[i]] = 1 + hash1.get(s1[i], 0)
            hash2[s2[i]] = 1 + hash2.get(s2[i], 0)

        # O(N)
        if hash1 != hash2:
            self.cache[(s1, s2)] = False
            return False

        # O(N)
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or
                    self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                self.cache[(s1, s2)] = True
                return True

        self.cache[(s1, s2)] = False
        return False


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        # Initialize a 3D table to store the results of all possible substrings of the two strings
        dp = [[[False for _ in range(n)] for _ in range(n)]
              for _ in range(n+1)]

        # Initialize the table for substrings of length 1
        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]

        # Fill the table for substrings of length 2 to n
        for length in range(2, n+1):
            for i in range(n+1-length):
                for j in range(n+1-length):
                    # Iterate over all possible lengths of the first substring
                    for newLength in range(1, length):
                        # Check if the two possible splits of the substrings are scrambled versions of each other
                        dp1 = dp[newLength][i]
                        dp2 = dp[length-newLength][i+newLength]
                        dp[length][i][j] |= dp1[j] and dp2[j+newLength]
                        dp[length][i][j] |= dp1[j+length-newLength] and dp2[j]

        # Return whether the entire strings s1 and s2 are scrambled versions of each other
        return dp[n][0][0]
