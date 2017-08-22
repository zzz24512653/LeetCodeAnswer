from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = defaultdict(lambda: 0)
        for n in nums:
            counter[n] += 1
        topk = sorted(counter.items(), key=lambda x: x[1], reverse=True)[:k]
        return [k for k, _ in topk]
