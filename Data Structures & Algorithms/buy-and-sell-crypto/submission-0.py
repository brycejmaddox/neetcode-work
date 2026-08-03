from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        starting_value = prices[0]
        best_profit = 0
        for i,price in enumerate(prices):
            if price - starting_value <= best_profit and price < starting_value:
                starting_value = price
                continue
            elif price - starting_value > best_profit:
                best_profit = price - starting_value
            else:
                continue
            
        return best_profit
    

