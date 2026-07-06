class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1} # what should be already be initialized as base case 

        def dfs(num):
            if num in dp:
                return dp[num]
            
            max_val = num if num != n else 0

            for i in range(1, num):
                curr = dfs(i) * dfs(num-i)
                max_val = max(max_val, curr)
            dp[num] = max_val 
            return dp[num]
        return dfs(n)
