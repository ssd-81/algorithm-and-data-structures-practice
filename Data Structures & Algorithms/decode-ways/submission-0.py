class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) +1)
        dp[0] = 1
        for i in range(1, len(s)+1):
            
            if s[i-1] in "123456789":
                dp[i] += dp[i-1]
            
            if i > 1 and (s[i-2:i][0] == "1" or (s[i-2:i][0] == "2" and s[i-2:i][1] in "0123456")):
                dp[i] += dp[i-2]

        return dp[-1]            
        