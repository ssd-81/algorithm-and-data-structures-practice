class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0 , len(nums) - 1

        while l <= r:
            if target < nums[l]:
                return l
            elif target > nums[r]:
                return r + 1
            mid = l + (r - l)//2
            if target == nums[mid]:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l 