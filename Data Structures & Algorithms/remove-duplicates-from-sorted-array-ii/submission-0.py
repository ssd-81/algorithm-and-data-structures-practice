class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0 
        hashMap = {}
        for r in range(len(nums)):
            if nums[r] not in hashMap:
                hashMap[nums[r]] = 0 
            hashMap[nums[r]] += 1

            if hashMap[nums[r]] <= 2:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            
        return l 
            
