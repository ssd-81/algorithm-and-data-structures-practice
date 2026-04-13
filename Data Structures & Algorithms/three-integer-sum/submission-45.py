class Solution:
    # this solution fails one of the final test cases
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        r_initial = len(nums) - 1
        i = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r =  r_initial 

            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if curSum < 0:
                    l += 1
                elif curSum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while (l < r and nums[l] == nums[l - 1]):
                        l += 1
        return res 