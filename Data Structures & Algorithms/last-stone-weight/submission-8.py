class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            t1 = heapq.heappop(max_heap)
            t2 = heapq.heappop(max_heap)

            if t1 > t2:
                t3 = t1 - t2
                heapq.heappush(max_heap, -t3)
            elif t2 > t1:
                t3 = t2 - t1 
                heapq.heappush(max_heap, -t3)
        return -max_heap[0] if len(max_heap) == 1 else 0
