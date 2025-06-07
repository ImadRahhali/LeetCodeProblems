# Last updated: 6/7/2025, 3:35:21 PM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            preMap[a].append(b)
       
        visited = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)

            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visited.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True