class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low = prices[0]
        counter = 1
        profit  = 0

        if len(prices) == 1:
            return 0

        while counter < len(prices):
            if prices[counter] < low:
                low = prices[counter]
            profit = max(profit, prices[counter] - low)
            counter += 1

        return profit