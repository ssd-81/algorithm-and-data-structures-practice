class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False 
        # approach
        # build all possible subsets and check for each if it sums to nums//2
        # if yes, return True; else False 

        required = sum(nums)//2
        def backtrack(idx, curr_sum):
            if curr_sum == required:
                return True 
            if curr_sum > required or idx == len(nums):
                return False 
            
            # choice 1: include nums[idx]
            if backtrack(idx + 1, curr_sum + nums[idx]):
                return True

            # choice 2: exclude nums[idx]
            if backtrack(idx + 1, curr_sum):
                return True
                
            
        res = set()
        for num in nums:
            res.add(num)
            if backtrack(0, 0):
                return True 
            res.remove(num)
        return False 