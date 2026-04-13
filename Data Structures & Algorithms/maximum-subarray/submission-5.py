class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0 
        maxSum = nums[0]
        maxL, maxR = 0, 0 
        L = 0 

        for R in range(len(nums)):
            
            if curSum < 0:
                L = R
                curSum = 0 
            curSum += nums[R]

            if curSum > maxSum:
                maxL, maxR = L, R
                maxSum = curSum 
        return sum(nums[maxL:maxR + 1])

        