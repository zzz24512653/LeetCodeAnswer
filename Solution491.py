class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sequences = [[]]
        for n in nums:
            t = []
            for s in sequences:
                if len(s) == 0:
                    t.append([n])
                elif n >= s[-1]:
                    k = s[:]
                    k.append(n)
                    t.append(k)
            sequences.extend(t)

        target_sequences = [s for s in sequences if len(s) > 1]

        filtered_sequences = set([','.join([str(t) for t in s]) for s in target_sequences])

        ret = [[int(t) for t in s.split(',')] for s in filtered_sequences]

        return ret
