class Solution(object):
    """
    1. 最暴力的方法是n2的，那么应该很自然地想到所需的方法是个nlog(n)的方法，如折半查找！
    2. 抽屉原理，11个数字放到10个盒子，那么至少有一个盒子里面有2个数字
    """
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 1
        high = len(nums) - 1
        while low != high:
            mid = (low + high) / 2
            count = 0
            for n in nums:
                if n <= mid:
                    count += 1
            if count <= mid:
                low = mid + 1
            else:
                high = mid
        return low
