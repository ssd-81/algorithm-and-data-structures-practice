class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # bitwise operation solution 

        x = n 
        x1 = n - 1

        return x > 0 and (x & x1) == 0 