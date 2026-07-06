class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [[0] * (len(profit) + 1) for _ in range(capacity + 1)]

        for cap in range(1, capacity+1):
            for i in range(1, len(profit)+1):
                if weight[i-1] <= cap:
                    # dp[cap][i+1] = max(profit[i] + dp[cap-weight[i]][i+1], dp[cap][i])
                    dp[cap][i] = max(profit[i-1] + dp[cap-weight[i-1]][i-1], dp[cap][i-1])
                else:
                    # dp[cap][i+1] = max(dp[cap][i],dp[cap-1][i+1] ) # not sure if this assignment is corred
                    # dp[cap][i+1] = max(dp[cap][i],dp[cap-1][i] )
                    dp[cap][i] = dp[cap][i-1]
        return dp[-1][-1]