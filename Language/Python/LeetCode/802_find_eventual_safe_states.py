from typing import List
from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}

        def dfs(i:int):
            if i in safe:
                return safe[i]
            
            safe[i] = False
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            
            safe[i] = True
            return True

        res = []
        for i in range(n):
            if dfs(i) == True:
                res.append(i)
        
        return res

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adjRev = [[] for _ in range(len(graph))]
        indegree = [0 for _ in range(len(graph))] 
        for pos, lst in enumerate(graph):
            for i in lst:
                adjRev[i].append(pos)
                indegree[pos]+=1 
    
        queue = deque()
        safenodes = []

        for i in range(len(graph)):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            safenodes.append(node)
            for i in adjRev[node]:
                indegree[i]-=1
                if(indegree[i] == 0):
                    queue.append(i)

        safenodes.sort()
        return safenodes