class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}

        def dfs(num):
            if num in dp:
                return dp[num]
            
            max_val = num

            for i in range(1, num):
                curr = dfs(i) * dfs(num-i)
                max_val = max(max_val, curr)
            dp[num] = max_val 
            return dp[num]
        ans = 0 
        for i in range(1, n):
            ans = max(ans, dfs(i) * dfs(n-i))
        return ans
