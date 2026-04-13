class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0 
        prefixSums = {0: 1}

        for n in nums: 
            curSum += n 
            diff = curSum - k 
            if curSum not in prefixSums: 
                prefixSums[curSum] = 0

            if diff in prefixSums:
                res += prefixSums[diff]
            prefixSums[curSum] += 1
        return res 