class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = l + (r - l) // 2
            res = min(res, nums[mid])

            # left portion is sorted
            if nums[mid] >= nums[l]:
                # isn't this always going to be true
                l = mid + 1
            # right portion is sorted
            else:
                r = mid - 1 
        return res 
                