from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, left = 0, 0

        # Check for profit from the prices
        for right in range(1, len(prices)):
            if prices[right] > prices[left]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
        
        return max_profit