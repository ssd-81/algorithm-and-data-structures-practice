class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        storeHash = {}
        for i in nums:
            if i not in storeHash: 
                storeHash[i] = 0
            storeHash[i] += 1
            
        maxFreq = 0
        maxElement = 0
        for k in storeHash:
            if storeHash[k] > maxFreq:
                maxFreq = storeHash[k]
                maxElement = k

        return maxElement
