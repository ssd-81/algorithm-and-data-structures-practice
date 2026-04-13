class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)

        firstMissing = 1

        for i in sortedNums:
            if i == firstMissing:
                firstMissing += 1
        return firstMissing
        