class Solution:
    def climbStairs(self, n: int) -> int:
        base = [1, 2]

        for i in range(n - 2):
            newVal = base[0] + base[1]
            base[0] = base[1]
            base[1] = newVal 
        
        return base[1] if n > 1 else 1