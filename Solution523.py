class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums is None or len(nums) < 2:
            return False
        dp = []
        for i in range(len(nums)):
            dp.append([nums[i]])
        for j in range(1, len(nums)):
            for i in range(len(nums)-j):
                t = nums[i+j]+dp[i][j-1]
                dp[i].append(t)
                if (k != 0 and t % k == 0) or (k == t):
                    return True
        return False
