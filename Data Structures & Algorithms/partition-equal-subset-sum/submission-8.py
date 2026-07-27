class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False 
        
        target = sum(nums) // 2 

        def dfs(idx, memo):
            if idx == len(nums):
                return False 
            if target in memo:
                return True 
            new_set = set()
            
            for i in memo:
                new_set.add(nums[idx] + i)
            memo = new_set | memo
            return dfs(idx + 1, memo)        
        return dfs(0, set([0]))