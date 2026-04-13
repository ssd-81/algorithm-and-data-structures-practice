class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        check_val = len(nums) // 3

        hashSet = {}
        returnArr = []
        for val in nums:
            if val not in hashSet:
                hashSet[val] = 0
            hashSet[val] += 1

        for key, val in hashSet.items():
            if val > check_val:
                returnArr.append(key)
        
        return returnArr
