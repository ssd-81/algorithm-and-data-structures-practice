class Solution:
    # we are given an array in increasing order
    # need to remove the duplicates in place 
    # each element appears only once

    # need to return the number of unique elements k 
    # first k elements of num contain unique elements
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = 0
        while r < n:
            nums[l] = nums[r]
            while r < n and nums[r] == nums[l]: 
                r += 1
            l += 1
        return l 

