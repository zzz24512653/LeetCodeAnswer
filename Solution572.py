# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def is_same(self, s, t):
        if s == t:
            return True
        if s is None or t is None:
            return False
        if s.val == t.val and self.is_same(s.left, t.left) and self.is_same(s.right, t.right):
            return True
        else:
            return False

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == t:
            return True
        if s is None or t is None:
            return False
        if self.is_same(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
