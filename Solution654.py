# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def construct(self, nums, i, j):
        if i == j:
            return TreeNode(nums[i])
        if j < i:
            return None
        max_index = i
        for k in range(i, j + 1):
            if nums[k] > nums[max_index]:
                max_index = k
        root = TreeNode(nums[max_index])
        root.left = self.construct(nums, i, max_index - 1)
        root.right = self.construct(nums, max_index + 1, j)
        return root

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums is None or len(nums) == 0:
            return None
        return self.construct(nums, 0, len(nums) - 1)

