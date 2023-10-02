class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        queue = deque()
        for x in rooms[0]:
            queue.append(x)
        visited = set([0])

        while queue:    
            x = queue.pop()
            visited.add(x)
            for i in rooms[x]:
                if i not in visited:
                    queue.append(i)            
            
        return len(visited) == n
