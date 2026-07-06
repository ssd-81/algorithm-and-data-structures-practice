class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}

        for i in range(len(nums)):
            counter_val = target - nums[i]

            if counter_val in hash_map:
                return [hash_map[counter_val], i]
            hash_map[nums[i]] = i
        
        return [-1, -1]