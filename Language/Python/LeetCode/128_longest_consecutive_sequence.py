class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.size = 1


class UnionFind:

    def find(self, node):
        if node.parent != node:
            node.parent = self.find(node.parent)
        return node.parent

    def union(self, node1, node2):
        parent_1 = self.find(node1)
        parent_2 = self.find(node2)
        if parent_1 != parent_2:
            parent_2.parent = parent_1
            parent_1.size += parent_2.size
        return parent_1.size


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind()
        nodes = {}
        max_size = 0
        for num in nums:
            if num not in nodes:
                node = Node(num)
                nodes[num] = node
                size = 1
                if num + 1 in nodes:
                    size = uf.union(node, nodes[num+1])
                if num - 1 in nodes:
                    size = uf.union(node, nodes[num-1])
                max_size = max(max_size, size)

        return max_size


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        parents = {num: num for num in nums}
        rank = {num: 1 for num in nums}
        nums_set = set(nums)

        def find(node):
            if node != parents[node]:
                node = find(parents[node])
            return node

        def union(node_1, node_2):
            par_1, par_2 = find(node_1), find(node_2)

            if par_1 != par_2:
                parents[par_2] = parents[par_1]
                rank[par_1] += rank[par_2]

            return rank[par_1]

        res = 1
        for num in nums_set:
            temp = res
            if num-1 in nums_set:
                temp = union(num, num-1)

            res = max(res, temp)

        return res
