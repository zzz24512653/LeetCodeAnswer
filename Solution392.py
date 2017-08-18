class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None:
            return False
        m = len(s)
        n = len(t)
        if m > n:
            return False
        if m == 0:
            return True
        j = 0
        for i in range(m):
            while j < n and s[i] != t[j]:
                j += 1
            if i == m-1:
                if j <= n-1:
                    return True
                else:
                    return False
            j += 1
        return False
