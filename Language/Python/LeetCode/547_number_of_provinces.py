class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n= len(isConnected)
        graph = {i: set() for i in range(n)}

        for row in range(n):
            for col in range(n):
                if isConnected[row][col] == 1 and row != col:
                    graph[row].add(col)
                    graph[col].add(row)
        
        # print(f"{graph = }, {isConnected = }")
        count = 0
        
        visited = set()
        queue = deque()
        while len(graph.keys()) != 0:
            count += 1
            queue.append(list(graph.keys())[0])
            # print("main. queue" , queue)
            while queue:
                element = queue.pop()
                if element in visited:
                    continue
                
                visited.add(element)
                # print(element, visited, graph)
                for nei in graph[element]: 
                    if nei not in visited:
                        queue.append(nei)
                
                del graph[element]
        
        return count


class Solution:
    def findCircleNum(self, is_connected: list[list[int]]) -> int:
        def visit_from(x: int, seen: set[int]) -> bool:
            return seen.add(x) or all(visit_from(y, seen) for y, c in enumerate(is_connected[x]) if y not in seen and c)

        seen = set()
        return sum((x not in seen) and visit_from(x, seen) for x in range(len(is_connected)))



from itertools import product

class DSU():
    def __init__(self, n):
        self.parents = {x: x for x in range(n)}
        self.sizes = {x: 1 for x in range(n)}
        self.count = n

    def find(self, u):
        if self.parents[u] != u:    
            return self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        ur, vr = self.find(u), self.find(v)
        if ur == vr:
            return
        
        if self.sizes[ur] < self.sizes[vr]:
            low, high = ur, vr
        else:
            low, high = vr, ur
        
        self.parents[low] = high
        self.sizes[high] += self.sizes[low]
        self.count -= 1
 
    def is_connected(self, u, v) -> bool:
        return self.find(u) == self.find(v)

    def ds_count(self) -> int:
        return self.count
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        edges = filter(lambda x: isConnected[x[0]][x[1]], product(range(n), range(n)))
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)
        return dsu.ds_count()


