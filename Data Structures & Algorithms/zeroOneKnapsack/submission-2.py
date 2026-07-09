class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [[0]*(len(weight)+1) for _ in range(capacity+1)] # items -> col , capacity -> rows 

        num_of_items = len(weight)
        for cap in range(1, capacity+1):
            for it in range(num_of_items):
                if weight[it] <= cap:
                    dp[cap][it+1] = max(profit[it] + dp[cap-weight[it]][it], dp[cap][it])
                else:
                    dp[cap][it+1] = dp[cap][it]
        
        return dp[-1][-1]