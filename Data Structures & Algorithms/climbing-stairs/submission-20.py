class Solution:
    def climbStairs(self, n: int) -> int:
        


        mem = {}

        def climb(n):
            if n in mem:
                return mem[n]
            if n == 1:
                mem[n] = 1
                return 1
            elif n == 2:
                mem[n] = 2
                return 2
            else:
                mem[n] = climb(n - 1) + climb(n -2)
                return mem[n]

        return climb(n)