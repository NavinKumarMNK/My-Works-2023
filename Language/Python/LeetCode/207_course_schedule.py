from collections import defaultdict,deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, p: List[List[int]]) -> bool:
        def topo(adj,v):
            indeg=[0]*v
            for q in adj.values():
                for i in q:
                    indeg[i]+=1
            q=deque()
            for i in range(len(indeg)):
                if indeg[i]==0:
                    q.append(i)
            order=[]
            while len(q)!=0:
                temp=q.popleft()
                order.append(temp)
                for a in adj[temp]:
                    indeg[a]-=1
                    if indeg[a]==0:
                        q.append(a)
            return order
        adj=defaultdict(list)
        for item in p:
            adj[item[1]].append(item[0])
        return len(topo(adj,numCourses))==numCourses

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visitSet = set()
        def dfs(crs):
            if crs in visitSet: return False
            if preMap[crs] == []: return True

            visitSet.add(crs)
            for i in preMap[crs]:
                if not dfs(i): return False

            visitSet.remove(crs)
            preMap[crs] = []
            return True     
        
        for crs in range(numCourses): 
            if not dfs(crs): return False
        
        return True
