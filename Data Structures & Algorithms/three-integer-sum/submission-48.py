class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        print(nums)
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            
            if(i > 0 and nums[i] == nums[i - 1]):
                continue
            while l < r:
                value = nums[i] + nums[l] + nums[r]
                if value == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l +=1
                elif value > 0:
                    r -= 1
                else:
                    l += 1
        return res