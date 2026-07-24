class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        requirements = [0] * numCourses 
        hashMap = {}

        for course, prereq in prerequisites:
            requirements[course] += 1
            if prereq not in hashMap:
                hashMap[prereq] = []
            hashMap[prereq].append(course)

        queue = deque()
        for i in range(numCourses):
            if requirements[i] == 0:
                queue.append(i)
        
        total_courses = 0 
        while queue and total_courses != numCourses:
            cur = queue.popleft()
            total_courses += 1

            if(cur in hashMap):
                for c in hashMap[cur]:
                    requirements[c] -= 1
                    if requirements[c] == 0:
                        queue.append(c)
        
        return total_courses == numCourses 
    









