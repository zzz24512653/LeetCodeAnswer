class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) < 2:
            return 0
        ret = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                ret += (prices[i] - prices[i-1])
        return ret
