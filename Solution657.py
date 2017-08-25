class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        i = 0
        j = 0
        for c in moves:
            if c == 'R':
                j += 1
            elif c == 'L':
                j -= 1
            elif c == 'D':
                i += 1
            else:
                i -= 1
        return i == 0 and j == 0
