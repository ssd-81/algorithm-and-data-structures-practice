class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = 1
        productArr = [] 
        
        for i in range(len(nums)):
            j = 0
            temp = 1
            while(j < len(nums)):
                if(j != i):
                    temp *= nums[j]
                j += 1
            productArr.append(temp)
        
        return productArr