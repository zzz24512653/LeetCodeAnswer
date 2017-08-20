# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution(object):
    def traverse(self, root, counter, ret):
        if root is None:
            return 'NULL'
        subtree = str(root.val) + self.traverse(root.left, counter, ret) + self.traverse(root.right, counter, ret)
        if counter[subtree] == 1:
            ret.append(root)
        counter[subtree] += 1
        return subtree

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        ret = []
        counter = defaultdict(lambda: 0)
        self.traverse(root, counter, ret)
        return ret
