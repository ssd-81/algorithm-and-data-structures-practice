class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {}

        for c1, c2 in prerequisites:
            if c1 in preMap:
                preMap[c1].append(c2)
            else:
                preMap[c1] = [c2]
        
        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if not preMap.get(course):
                return True
            visit.add(course)

            for nei in preMap[course]:
                if (not dfs(nei)):
                    return False
            visit.remove(course)
            # optimization 
            preMap[course] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True 
             
