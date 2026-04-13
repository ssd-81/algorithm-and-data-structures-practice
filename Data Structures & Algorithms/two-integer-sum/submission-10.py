class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]].append(i)
            else:
                hashMap[nums[i]] = [i]
        
        for val in hashMap:
            temp = target - val
            if temp in hashMap:
                if temp == val:
                    if len(hashMap[val]) == 2:
                        return [hashMap[val][0], hashMap[val][1]]
                else:
                    return [hashMap[val][0], hashMap[temp][0]]
