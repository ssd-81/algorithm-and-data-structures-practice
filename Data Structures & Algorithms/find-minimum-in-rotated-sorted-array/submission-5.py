class Solution:
    def findMin(self, nums: List[int]) -> int:
        # when array is rotated; array is split into two halves(if)
        # the left half has all values greater than all values 
        # in the right half 

        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                return res 
            mid = (l + r) // 2
            res = min(res, nums[mid])
            
            # left half is sorted 
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:  
                r = mid - 1
        return res 
            