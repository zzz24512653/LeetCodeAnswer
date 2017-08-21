class Solution(object):
    def multiply(self, l1, l2):
        ret = []
        for li in l1:
            for lj in l2:
                t = li[:]
                t.extend(lj[:])
                ret.append(t)
        return ret


    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) < 1:
            return [[]]
        ret = [[], [nums[0]]]
        for i in range(1, len(nums)):
            ret = self.multiply(ret, [[], [nums[i]]])
        return ret
