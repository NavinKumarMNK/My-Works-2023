from typing import List
import collections
import heapq


class Solution:
    # Time Complexity : Dijiktra's => O(ElogV)
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        print(f"{edges = }")

        min_heap = [(0, k)]  # (distance_from_main, node_pos)
        visit = set()

        time = 0
        while min_heap:
            (weight1, node1) = heapq.heappop(min_heap)
            if node1 in visit:
                continue
            visit.add(node1)
            time = max(time, weight1)

            for (neig, weight) in edges[node1]:
                if neig not in visit:
                    heapq.heappush(min_heap, (weight1 + weight, neig))

        return time if len(visit) == n else -1
