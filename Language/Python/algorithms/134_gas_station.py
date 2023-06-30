class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas): return -1
        gc = idx = 0
        for i in range(len(gas)):
            gc += gas[i] - cost[i]
            if gc < 0:
                gc = 0
                idx = i+1
        return idx
    