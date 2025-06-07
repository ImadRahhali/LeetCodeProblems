# Last updated: 6/7/2025, 3:43:48 PM
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        preMap = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            preMap[a].append(b)
        
        visited, path = set(), set()

        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
                
            path.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            path.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res