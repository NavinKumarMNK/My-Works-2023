class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hash_map = defaultdict(int)

        for i in wall:
            temp = 0
            for j in i[:-1]:
                temp += j
                hash_map[temp] += 1

        hash_map[len(wall)] = 0

        return len(wall)-max(hash_map.values())
