class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            hashMap[nums[i]] = i
        print(hashMap)
        
        for i in range(len(nums)):
            req = target - nums[i]
            if req in hashMap:
                return [i, hashMap[req]]
        