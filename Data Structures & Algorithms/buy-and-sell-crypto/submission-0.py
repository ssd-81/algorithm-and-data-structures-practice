class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices[i] is the price of stock on the ith day
        # choose a single day to buy one NeetCoin and choose 
        # a different day in future to sell it 

        possibleOptions = []
        for i in range(len(prices)):

            for j in range(i, len(prices)):
                possibleOptions.append((prices[i], prices[j]))
        
        maxProfit = 0
        for buy, sell in possibleOptions:
            if sell - buy > maxProfit:
                maxProfit = sell - buy
        
        return maxProfit 