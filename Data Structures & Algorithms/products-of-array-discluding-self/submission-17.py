class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # creating two arrays for prefix and suffix sums 
        prefix_prod = [1] * len(nums)
        suffix_prod = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix_prod[i] = prefix_prod[i-1] * nums[i-1]
        
        prod_so_far = 1
        for i in range(len(nums)-1, -1, -1):
            suffix_prod[i] = prod_so_far
            prod_so_far *= nums[i]
        
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix_prod[i] * suffix_prod[i]
        return res 