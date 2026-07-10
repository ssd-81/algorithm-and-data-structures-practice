class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)

        X = min(nums)
        LIS = 0 
        while X in hash_set:
            LIS += 1
            X = X + 1
        
        return LIS 