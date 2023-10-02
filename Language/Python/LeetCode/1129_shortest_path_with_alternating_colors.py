import collections

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = collections.defaultdict(list)
        blue = collections.defaultdict(list)

        for (n1, n2) in redEdges:
            red[n1].append(n2)
        for (n1, n2) in blueEdges:
            blue[n1].append(n2)

        answer = [-1 for _ in range(n)]
        answer[0] = 0
        queue = collections.deque()
        queue.append([0, 0, None]) # Cost, Node, prev_color
        visited = set((0, None))  # First Visited 0   

        while queue:
            element = queue.popleft()
            visited.add((element[1], element[2]))
            
            if answer[element[1]] == -1:
                answer[element[1]] = element[0]

            if element[2] != "r":
                for nei in red[element[1]]:
                    if (nei, 'r') not in visited:
                        queue.append([element[0]+1, nei, 'r'])
            if element[2] != "b":
                for nei in blue[element[1]]:
                    if (nei, 'b') not in visited:
                        queue.append([element[0]+1, nei, 'b'])

        return answer
