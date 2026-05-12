class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            while i > 0 and i < len(nums) and  nums[i] == nums[i - 1]:
                i += 1

            l, r = i + 1 ,len(nums) - 1 
            while l < r:
                currSum = nums[l] + nums[r] + nums[i]

                if currSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif currSum > 0:
                    r -= 1
                else:
                    l += 1
        return res 
