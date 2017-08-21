class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) < 2:
            return 0
        pre_min = prices[0]
        ret = 0
        for p in prices:
            if p - pre_min > ret:
                ret = p - pre_min
            if p < pre_min:
                pre_min = p
        return ret
