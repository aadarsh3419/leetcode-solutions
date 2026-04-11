class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit  = float('inf')
        profit = 0
        for price in prices:
            if price < min_profit:
                min_profit = price
            else:
                profit = max(profit,price - min_profit)
        return profit


















        
