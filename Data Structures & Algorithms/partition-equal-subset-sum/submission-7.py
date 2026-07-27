class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False 
        
        target = sum(nums) // 2 
        possible_values = set()

        def dfs(idx, val_set, cur_sum):
            if idx == len(nums):
                return False
            if cur_sum == target:
                return True
            
            for i in range(idx, len(nums)):
                cur_sum += nums[i]
                if dfs(i + 1, val_set, cur_sum):
                    return True
                cur_sum -= nums[i]
            return False 
        return dfs(0, list(), 0)
        



