class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = collections.defaultdict(list)  # Mgr -> [list of emps]
        for i in range(n):
            adj[manager[i]].append(i)

        # BFS
        q = deque([(headID, 0)])  # (id, time)
        res = 0
        while q:
            i, time = q.popleft()
            res = max(res, time)
            for emp in adj[i]:
                q.append((emp, time + informTime[i]))
        return res

