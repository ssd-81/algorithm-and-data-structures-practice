class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        curr_sum = 0 

        hash_map = defaultdict(int)
        hash_map[0] = 1
        valid_subarrays = 0 
        for i in range(len(nums)):
            curr_sum += nums[i]
            target = curr_sum - k
            if target in hash_map:
                valid_subarrays += hash_map[target]
            hash_map[curr_sum] += 1
        return valid_subarrays