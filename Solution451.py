from collections import defaultdict


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) < 2:
            return s
        counter = defaultdict(lambda: 0)
        for c in s:
            counter[c] += 1
        return ''.join([k*v for k, v in sorted(counter.items(), key=lambda x: x[1], reverse=True)])
