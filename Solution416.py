class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = sum(nums)
        n = len(nums)
        if m % 2 != 0 or n < 2:
            return False
        dp = [[set([0])] for _ in range(2)]
        for i in range(n):
            dp[0].append(set([x+nums[i] for x in dp[0][i].union(dp[1][i])]))
            dp[1].append(dp[0][i].union(dp[1][i]))
            if m/2 in dp[0][i+1] or m/2 in dp[1][i+1]:
                return True
        return False
