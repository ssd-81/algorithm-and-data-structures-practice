class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        last = [1] * n

        for i in range(m-1):
            for j in range(n-2, -1, -1):
                last[j] = last[j] + last[j+1]
        
        return last[0]