class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1

        dp = [[0]]
        for _ in range(1, m):
            dp.append([1])
        for _ in range(1, n):
            dp[0].append(1)

        for i in range(1, m):
            for j in range(1, n):
                dp[i].append(dp[i][j-1] + dp[i-1][j])

        return dp[m-1][n-1]
