class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hash_map = defaultdict(int)
        valid_subarrays = 0 

        prefix_sum = [0] * (len(nums)+1)
        valid_subarrays = 0 

        for i in range(len(nums)):
            prefix_sum[i+1] = nums[i] + prefix_sum[i]
        for prefix in prefix_sum:
            target = prefix - k 
            if target in hash_map:
                valid_subarrays += hash_map[target]
            hash_map[prefix] += 1
        return valid_subarrays 
        
