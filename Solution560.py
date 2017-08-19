from collections import defaultdict

'''
1. 求数组中(i,j]之间的sum值可以用[0-j]的sum - [0-i]的sum
2. 用字典保存当前值之前的所有sum的次数
3. counter[0]=1是处理当前值==k的情况
'''


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = defaultdict(lambda: 0)
        counter[0] = 1
        ret = 0
        cur_sum = 0
        for n in nums:
            cur_sum += n
            ret += counter[cur_sum - k]
            counter[cur_sum] += 1
        return ret
