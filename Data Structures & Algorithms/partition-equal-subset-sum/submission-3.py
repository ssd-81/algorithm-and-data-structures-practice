class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False 
        
        target = sum(nums) // 2 
        values_set = set()

        def dfs(idx, val_set, cur_sum):
            if idx == len(nums):
                return []
            if cur_sum == target:
                return val_set[:]
            
            for i in range(idx, len(nums)):
                val_set.append(nums[i])
                cur_sum += nums[i]
                res =  dfs(idx + 1, val_set, cur_sum)
                if res != []:
                    return True
                val_set.pop()
                cur_sum -= nums[i]
            return False 
        return dfs(0, list(), 0)
        



