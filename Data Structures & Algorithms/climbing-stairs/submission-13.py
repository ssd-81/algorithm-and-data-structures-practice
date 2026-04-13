class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        stairWays = {}
        if n in stairWays:
            return stairWays[n]
        
        stairWays[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
        return stairWays[n]
        