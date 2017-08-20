# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution(object):
    def search(self, root, sum, paths):
        if root is None:
            return defaultdict(lambda: 0)
        left_sums = self.search(root.left, sum, paths)
        right_sums = self.search(root.right, sum, paths)
        ret = defaultdict(lambda: 0)
        ret[root.val] += 1
        for k, v in left_sums.items():
            ret[k + root.val] += v
        for k, v in right_sums.items():
            ret[k + root.val] += v
        paths.append(ret[sum])
        return ret

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        paths = []
        self.search(root, sum, paths)
        ret = 0
        for p in paths:
            ret += p
        return ret
