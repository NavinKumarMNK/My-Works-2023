from typing import List


class Solution:
    """
    Time Complexity: O(sum(len(word)))
    Space Complexity: O(sum(len(word)) + sum(unique_chars)
                     + min(sum(unique_chars)**2, len(words))
    """

    def alienOrder(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        print(f"{adj = }")

        visit = {}  # False=visited, True=visited & current path
        res = []

        def dfs(node: str) -> bool | None:
            if node in visit:
                return visit[node]

            visit[node] = True

            for neig in adj[node]:
                if dfs(neig):
                    return True

            visit[node] = False
            res.append(node)

        for node in adj:
            if dfs(node):
                return ""

        return "".join(res[::-1])


if __name__ == "__main__":
    sol = Solution()
    assert sol.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]) == "wertf"
