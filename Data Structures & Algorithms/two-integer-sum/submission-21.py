class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = []
            hashMap[nums[i]].append(i)
        print(hashMap)
        
        for i in range(len(nums)):
            req = target - nums[i]
            if req in hashMap:
                for idx in hashMap[req]:
                    if idx != i:
                        return [i, idx]
            

                
        