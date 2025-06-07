# Last updated: 6/7/2025, 2:10:14 PM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            pre[a].append(b)
        
        visited, path = set(), set()
        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True

            path.add(node)

            for prereq in pre[node]:
                if not dfs(prereq):
                    return False
            path.remove(node)
            visited.add(node)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True



