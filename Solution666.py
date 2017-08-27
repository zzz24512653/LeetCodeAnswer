from collections import defaultdict


class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = defaultdict(lambda: 0)
        for n in nums:
            i = int(n / 100)
            j = int((n % 100) / 10)
            k = n % 10
            counter[2 ** (i-1) - 2 + j] = k
        ret = 0
        for k, v in counter.items():
            if (2*k+1) not in counter and (2*k+2) not in counter:
                path_sum = 0
                parent = k
                while parent >= 0:
                    path_sum += counter[parent]
                    if parent % 2 == 0:
                        parent = (parent-2) / 2
                    else:
                        parent = (parent-1) / 2
                ret += path_sum
        return ret
