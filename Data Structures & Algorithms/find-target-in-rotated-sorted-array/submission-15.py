class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1
        # 1, 0 , 1, 1, 1
        # 1, 1, 3, 1 target = 3 
        while l < r:
            m = l + (r-l) //2

            if nums[m] == target:
                return m
            # left portion is sorted
            if nums[m] > nums[l]:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m 
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m 
        return -1