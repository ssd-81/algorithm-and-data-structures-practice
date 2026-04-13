class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashStore = {}

        for i in nums:
            if hashStore.get(i) == True:
                return True
            hashStore[i] = True 
        return False 
        