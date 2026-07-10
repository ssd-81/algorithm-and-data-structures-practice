class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time: O(n) 

        numsSet = set(nums)
        longest = 0 

        for n in nums:
            # check if its the start of a sequence 
            if (n-1) not in numsSet:
                length = 0 
                while (n + length) in numsSet:
                    length += 1
                longest = max(length, longest)
        return longest 