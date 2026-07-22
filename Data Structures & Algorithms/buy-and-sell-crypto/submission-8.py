class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        profit = 0 

        for i in range(1, len(prices)):
            if prices[i] - min_so_far > profit:
                profit = prices[i] - min_so_far 
            
            min_so_far = min(prices[i], min_so_far)
        return profit 