# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def post_traverse(self, root, sums):
        if root is None:
            return 0
        left_sum = self.post_traverse(root.left, sums)
        right_sum = self.post_traverse(root.right, sums)
        sums.append(left_sum + right_sum + root.val)
        return left_sum + right_sum + root.val

    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        sums = []
        self.post_traverse(root, sums)
        for i in range(len(sums) - 1):
            if sums[i] * 2 == sums[-1]:
                return True
        return False
