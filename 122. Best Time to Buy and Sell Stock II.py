from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        # Check for profit from the prices
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                max_profit += (prices[i] - prices[i-1])
        
        return max_profit