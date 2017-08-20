# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''
        if t.left is None and t.right is None:
            return str(t.val)
        ret = str(t.val) + '(' + self.tree2str(t.left) + ')'
        if t.right is not None:
            ret += '(' + self.tree2str(t.right) + ')'
        return ret