class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l = 0  
        max_so_far = float('-inf')

        for i in range(len(nums)):
            if nums[i] > max_so_far:
                max_so_far = nums[i]
                nums[l] = nums[i] 
                l += 1
        
        return l 
