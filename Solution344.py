class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = []
        for i in range(len(s)-1, -1, -1):
            ret.append(s[i])
        return ''.join(ret)
