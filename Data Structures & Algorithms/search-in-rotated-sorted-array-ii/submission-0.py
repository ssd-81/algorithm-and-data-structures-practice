class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # nums = [3,4,4,5,6,1,2,2], target = 1
        # decrease operation steps as much as possible

        l, r = 0, len(nums)-1

        while l < r:
            m = l + (r-l)//2

            if nums[m] == target:
                return True 
            # left portion is sorted
            if nums[m] >= nums[l]:
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m 
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m 
        return False

            
