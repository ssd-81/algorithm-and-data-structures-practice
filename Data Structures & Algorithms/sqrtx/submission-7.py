class Solution:
    def mySqrt(self, x: int) -> int:
        # sqrt x rounded down to nearest integer
        # z * z = x
        # z = x/z
        
        # i * i = x; i * i <  x ; i * i > x
        if x == 0:
            return 0
        if x == 1:
            return 1 
        for i in range(x//2 + 1):
            if i * i == x:
                return i
            elif i * i > x:
                return i - 1
