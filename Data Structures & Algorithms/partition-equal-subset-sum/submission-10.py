class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False 
        target = sum(nums) // 2
        
        def dfs(idx, remaining):
            if remaining == 0:
                return True
            if idx == len(nums):
                return False

            if dfs(idx+1, remaining - nums[idx]):
                return True 
            if dfs(idx + 1, remaining):
                return True 
            return False 
        return dfs(0, target)
