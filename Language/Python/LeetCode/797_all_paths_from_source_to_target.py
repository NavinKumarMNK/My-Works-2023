class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        
        def dfs(node, path, visited):
            visited.add(node)
            path.append(node)
            if node == len(graph) - 1:
                paths.append(path.copy())
            else:
                for nei in graph[node]:
                    if nei not in visited:
                        dfs(nei, path.copy(), visited.copy())
            path.pop()
            visited.remove(node)

        dfs(0, [], set())
        return paths

