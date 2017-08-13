class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return None
        dp = [nums[0]]
        ret = nums[0]
        for i in range(1, len(nums)):
            t = max(nums[i], dp[i-1]+nums[i])
            dp.append(t)
            if t > ret:
                ret = t
        return ret
