class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # kth largest => n-k smallest 

        # can I solve it using max heap 
        # how many elements will I have to maintain in max heap 

        top_k_max = [] 

        for idx, num in enumerate(nums):
            heapq.heappush(top_k_max, (num, idx))

            if len(top_k_max) == k+1:
                heapq.heappop(top_k_max)
        print(top_k_max[0])
        kth_largest, _ = heapq.heappop(top_k_max)
        return kth_largest