# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def search(self, root, cur_path, cur_sum, target, ret):
        if root is None:
            return
        cur_path.append(root.val)
        cur_sum += root.val
        if root.left is None and root.right is None and cur_sum == target:
            ret.append(cur_path)
        self.search(root.left, cur_path[:], cur_sum, target, ret)
        self.search(root.right, cur_path[:], cur_sum, target, ret)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ret = []
        self.search(root, [], 0, sum, ret)
        return ret
