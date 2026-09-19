class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target: return True 

            if nums[l] < nums[m]:
                if target >= nums[l] and target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            elif nums[l] > nums[m]:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m 
            else:
                l += 1

        return False 