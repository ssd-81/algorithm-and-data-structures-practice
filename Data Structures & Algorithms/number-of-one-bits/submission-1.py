class Solution:
    def hammingWeight(self, n: int) -> int:
        
        numOfOnes = 0
        while n > 0:
            if n & 1:
                numOfOnes += 1
            n = n >> 1
        return numOfOnes