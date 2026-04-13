class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        points_dis = []
        for i in points:
            points_dis.append((self.distanceFromOrigin(i), i))
        heapq.heapify(points_dis)
        kClosePoints = []
        while len(points_dis) > len(points) - k:
            temp = heapq.heappop(points_dis)
            kClosePoints.append(temp[1])
        return kClosePoints
        


    def distanceFromOrigin(self, point):
        return math.sqrt((point[0]**2 + point[1]**2))                
