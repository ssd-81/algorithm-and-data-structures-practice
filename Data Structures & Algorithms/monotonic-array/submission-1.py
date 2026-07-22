class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = True 
        decrease = True 

        for i in range(len(nums)):
            if i > 0 and increase:
                if nums[i] - nums[i-1] < 0:
                    increase = False 
            if i > 0 and decrease:
                if nums[i] - nums[i-1] > 0:
                    decrease = False 
                
        return increase or decrease 