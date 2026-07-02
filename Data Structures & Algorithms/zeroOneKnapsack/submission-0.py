class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        dp = [[0] * (capacity + 1) for _ in range(len(weight) + 1)]


        for c in range(1, capacity + 1):
            for i in range(1, len(weight) + 1):
                if weight[i-1] <= c:
                    dp[i][c] = max(profit[i-1] + dp[i-1][c-weight[i-1]], dp[i-1][c]) # cap or capacity
                else:
                    dp[i][c] = dp[i-1][c]
        return dp[-1][-1]