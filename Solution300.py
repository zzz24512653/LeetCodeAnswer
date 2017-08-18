class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return n
        dp = [1] * n
        ret = 1
        for i in range(1, n):
            cur_max = 1
            for j in range(i):
                if nums[j] < nums[i] and (dp[j] + 1) > cur_max:
                    cur_max = dp[j] + 1
            dp[i] = cur_max
            if cur_max > ret:
                ret = cur_max
        return ret
