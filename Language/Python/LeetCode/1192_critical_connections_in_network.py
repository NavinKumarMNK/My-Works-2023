class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for (n1, n2) in connections:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        tin = [ 0 for _ in range(n)] # time of insertion
        low = [10**9 for _ in range(n)] # lowest time of reach
        visited = [0 for _ in range(n)] # keep track of visited
        timer = 0
        bridges = []

        def dfs(parent, node):
            nonlocal timer
            timer+=1
            low[node] = tin[node] = timer 
            visited[node] = 1

            for nei in graph[node]:
                if nei == parent:
                    continue
                if not visited[nei]:
                    dfs(node, nei)
                    low[node] = min(low[nei], low[node])
                    if low[nei] > tin[node]:
                        bridges.append((node, nei))
                else:
                    low[node] = min(low[nei], low[node])

        dfs(None, 0)
        return bridges
        

