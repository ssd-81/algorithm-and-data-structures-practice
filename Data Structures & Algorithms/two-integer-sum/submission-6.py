class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            req = target - nums[i]
            if req not in hashMap.keys():
                hashMap[nums[i]] = i
            else:
                return sorted([i, hashMap[req]])