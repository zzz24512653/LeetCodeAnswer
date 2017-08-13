class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = []

        for i in range(0, m):
            dp.append([])
            if obstacleGrid[i][0] == 1 or (i > 0 and dp[i-1][0] == 0):
                dp[i].append(0)
            else:
                dp[i].append(1)

        for j in range(1, n):
            if obstacleGrid[0][j] == 1 or dp[0][j-1] == 0:
                dp[0].append(0)
            else:
                dp[0].append(1)

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i].append(0)
                elif dp[i-1][j] == 0:
                    dp[i].append(dp[i][j-1])
                elif dp[i][j-1] == 0:
                    dp[i].append(dp[i-1][j])
                else:
                    dp[i].append(dp[i-1][j] + dp[i][j-1])

        return dp[m-1][n-1]
