class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False 
        temp = n 

        while temp % 2 == 0:
            temp //= 2 
        return temp == 1