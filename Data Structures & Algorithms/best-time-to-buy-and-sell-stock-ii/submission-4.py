class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        l, r = 0, 1
        for i in range(0, len(prices)-1):
            if prices[l] < prices[r]:
                profit += prices[r] - prices[l]

            l += 1
            r += 1

        return profit 
