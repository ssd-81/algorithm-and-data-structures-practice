class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        maxSum = 0

        for num in nums:
            if (maxSum + num) < 0:
                maxSum = 0
            maxSum = max(num, maxSum + num)
            res = max(maxSum, res)
        return res 
            