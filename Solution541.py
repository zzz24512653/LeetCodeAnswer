class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ret = []
        n = len(s)
        for i in range(0, n, 2 * k):
            for j in range(i, i + 2*k):
                if j >= n:
                    break
                if j >= i + k:
                    ret.append(s[j])
                else:
                    ret.insert(i, s[j])
        return ''.join(ret)
