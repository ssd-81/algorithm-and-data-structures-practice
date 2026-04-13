class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = defaultdict(int)

        for i in range(len(nums)):
            hashMap[nums[i]] = i
        
        for i in range(len(nums)):
            if hashMap.get(target - nums[i]) and hashMap[target - nums[i]] != i:
                return sorted([hashMap[target - nums[i]], i])
        return []