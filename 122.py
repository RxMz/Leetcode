class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        Logic:
        	1) Basically add the net profits of each day only if the net profit is positive.
        	2) O(n)
        """
        return sum([max(prices[i + 1]- prices[i], 0) for i in range(len(prices) - 1)])
            