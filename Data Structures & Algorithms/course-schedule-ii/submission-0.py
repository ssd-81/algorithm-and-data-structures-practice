class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        requirements = [0] * numCourses 

        reqMapping = defaultdict(list)

        for course, prereq in prerequisites:
            requirements[course] += 1

            reqMapping[prereq].append(course)
        
        queue = deque([])
        for i in range(numCourses):
            if requirements[i] == 0:
                queue.append(i)
        res = []
        totalCourses = 0 
        while queue:
            cur = queue.popleft()
            res.append(cur)
            totalCourses += 1

            for i in reqMapping[cur]:
                requirements[i] -= 1

                if requirements[i] == 0:
                    queue.append(i)
        return res if totalCourses == numCourses else []


