class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = []
        for item in s.split(' '):
            t = []
            for c in item:
                t.insert(0, c)
            ret.append(''.join(t))
        return ' '.join(ret)
