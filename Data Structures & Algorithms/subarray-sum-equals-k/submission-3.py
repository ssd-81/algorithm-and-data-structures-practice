class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * (len(nums)+1)

        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        
        hashMap = {}
        res = 0 
        for num in prefix_sum:
            target = num - k
            if target in hashMap:
                res += hashMap[target]
            hashMap[num] = 1 + hashMap.get(num, 0)
        return res 