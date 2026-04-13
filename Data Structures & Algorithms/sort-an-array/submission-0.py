class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        numsCopy = nums.copy()
        
        for i in range(len(numsCopy)):
            for j in range(i , len(numsCopy)):
                if numsCopy[i] > numsCopy[j]:
                    temp = numsCopy[i]
                    numsCopy[i] = numsCopy[j]
                    numsCopy[j] = temp
        return numsCopy