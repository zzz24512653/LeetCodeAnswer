from collections import defaultdict


class Solution(object):
    def multiply(self, l1, l2):
        ret = []
        for li in l1:
            for lj in l2:
                t = li[:]
                t.extend(lj[:])
                ret.append(t)
        return ret

    def composite(self, n, t):
        ret = []
        for i in range(t+1):
            ret.append([n] * i)
        return ret

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) < 1:
            return [[]]
        ret = None
        counter = defaultdict(lambda: 0)
        for n in nums:
            counter[n] += 1
        for k, v in counter.items():
            if ret is None:
                ret = self.composite(k, v)
            else:
                ret = self.multiply(ret, self.composite(k, v))
        return ret
