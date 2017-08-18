class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums_sorted = sorted(nums)
        ret = 0
        for i in range(0, n, 2):
            ret += nums_sorted[i]
        return ret
