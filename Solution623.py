# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def construct(self, root, v, d):
        if root is None:
            return
        if d == 1:
            n1 = TreeNode(v)
            n1.left = root.left
            root.left = n1
            n2 = TreeNode(v)
            n2.right = root.right
            root.right = n2
            return
        self.construct(root.left, v, d - 1)
        self.construct(root.right, v, d - 1)

    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        self.construct(root, v, d - 1)
        return root
