class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit  = 0

        for counter in range(1,len(prices)):
            if prices[counter] < low:
                low = prices[counter]
            profit = max(profit, prices[counter] - low)

        return profit