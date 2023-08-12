class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(num_courses)}
        for crs, preq in prerequisites:
            prereq[crs].append(preq)

        output = []
        # visit[i]: False => currently visited , True => visited already
        visit = {}

        def dfs(crs):
            if crs in visit:
                return visit[crs]

            visit[crs] = False
            for pre in prereq[crs]:
                if dfs(pre) is False:
                    return False

            visit[crs] = True
            output.append(crs)

            return True

        for crs in range(num_courses):
            if dfs(crs) is False:
                return []

        return output
