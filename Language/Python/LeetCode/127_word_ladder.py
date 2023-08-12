from typing import List
import collections


class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        if end_word not in word_list:
            return 0

        nei = collections.defaultdict(list)  # neighbour list
        word_list.append(begin_word)
        # create adjacent Lis
        for word in word_list:
            for j in range(0, len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)

        visit = set([begin_word])
        q = collections.deque([begin_word])

        print(nei)

        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == end_word:
                    return res

                for j in range(0, len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei_word in nei[pattern]:
                        if nei_word not in visit:
                            visit.add(nei_word)
                            q.append(nei_word)

            res += 1

        return 0
