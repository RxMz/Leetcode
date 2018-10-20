class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
            1) Dynamically get the minimum cost and maximum profit while iterating.
            2) O(n) 
        """
        if len(prices) < 2:
            return 0
        max_profit, min_cost = 0, prices[0]
        for i in prices:
            profit = i - min_cost
            max_profit = max(profit, max_profit)
            min_cost = min(min_cost, i)
        return max_profit
            