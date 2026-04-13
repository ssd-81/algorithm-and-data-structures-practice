class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)

        for i in nums:
            hashMap[i] += 1
        
        for k in hashMap:
            if hashMap[k] > 1:
                return k
        