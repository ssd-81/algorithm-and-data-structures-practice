class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1 
        res = [1, 1]
        
        
        for i in range(n-1):
            res[0], res[1] = res[0] + res[1], res[0]

        return res[0]