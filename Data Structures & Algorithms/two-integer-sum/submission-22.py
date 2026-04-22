class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = []
            hashMap[nums[i]].append(i)
        
        for i in range(len(nums)):
            com = target - nums[i]

            if com in hashMap:
                for j in hashMap[com]:
                    if i != j:
                        return [i, j]
