class Solution:
    def climbStairs(self, n: int) -> int:
        first, second = 1, 2 
        if n <= 2:
            return first if n <= 1 else 2 

        for _ in range(n-2):
            temp = second 
            second = first + second 
            first = temp 
        return second 