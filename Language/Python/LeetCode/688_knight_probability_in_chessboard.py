class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        pos = [[-2, 1], [-2, -1],
               [-1, 2], [-1, -2],
               [1, 2], [1, -2],
               [2, 1], [2, -1]]

        @cache
        def jump(i, j, count):
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0

            if count == 0:
                return 1

            ret = 0
            for p in pos:
                ret += jump(i + p[0], j + p[1], count - 1)

            return ret

        total_moves = 8 ** k
        valid_moves = jump(row, column, k)
        probability = valid_moves / total_moves

        return probability
