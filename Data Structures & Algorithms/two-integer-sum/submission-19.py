class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            if target - num in hashMap and hashMap[target - num] != i:
                return [hashMap[target - num], i]
            else:
                hashMap[nums[i]] = i
        return []