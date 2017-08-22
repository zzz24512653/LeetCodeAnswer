class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s is None or len(s) <= numRows or numRows == 1:
            return s
        nums = [[] for _ in range(numRows)]
        for i, n in enumerate(s):
            t = i % (2 * numRows - 2)
            if t < numRows:
                nums[t].append(n)
            else:
                nums[2 * numRows -2 - t].append(n)
        return ''.join([''.join(line) for line in nums])
