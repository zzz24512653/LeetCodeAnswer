class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if nums is None or len(nums) == 0 or S > 1000:
            return 0
        n = len(nums)
        dp = [[0]*2001 for _ in range(n)]
        dp[0][1000+nums[0]] += 1
        dp[0][1000-nums[0]] += 1
        for i in range(1, n):
            for j in range(2000):
                if dp[i-1][j] != 0:
                    dp[i][j+nums[i]] += dp[i-1][j]
                    dp[i][j-nums[i]] += dp[i-1][j]
        return dp[n-1][1000+S]
