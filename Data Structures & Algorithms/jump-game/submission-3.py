class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        currReachable = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            
            if nums[i] + i >= currReachable:
                currReachable = i 
            
        return currReachable == 0 