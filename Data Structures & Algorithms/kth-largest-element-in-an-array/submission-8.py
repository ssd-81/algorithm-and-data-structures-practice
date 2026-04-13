class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth largest and not the kth distinct largest
        heapq.heapify(nums)
        
        while len(nums) > k:
            heapq.heappop(nums)
        
        return heapq.heappop(nums)
