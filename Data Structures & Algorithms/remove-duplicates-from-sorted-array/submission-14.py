class Solution:
    # we are given an array in increasing order
    # need to remove the duplicates in place 
    # each element appears only once

    # need to return the number of unique elements k 
    # first k elements of num contain unique elements
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l

