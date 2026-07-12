class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left:
            heapq.heappush(self.left, -num)
        elif num > -self.left[0]:
            heapq.heappush(self.right, num)

            if len(self.right) > len(self.left):
                first_right = heapq.heappop(self.right)
                heapq.heappush(self.left, -first_right)
        else:
            heapq.heappush(self.left, -num)

            if len(self.left) > len(self.right) + 1:
                last_left = heapq.heappop(self.left)
                heapq.heappush(self.right, -last_left)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0])/2
        return -self.left[0]
        
        