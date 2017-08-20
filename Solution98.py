# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def valid(self, root):
        is_bst = True
        cur_min = root.val
        cur_max = root.val
        if root.left is not None:
            (is_left_bst, tree_max, tree_min) = self.valid(root.left)
            is_bst = is_bst and is_left_bst
            if tree_max >= root.val:
                is_bst = False
            cur_min = min(cur_min, tree_min)
            cur_max = max(cur_max, tree_max)
        if root.right is not None:
            (is_right_bst, tree_max, tree_min) = self.valid(root.right)
            is_bst = is_bst and is_right_bst
            if tree_min <= root.val:
                is_bst = False
            cur_min = min(cur_min, tree_min)
            cur_max = max(cur_max, tree_max)
        return (is_bst, cur_max, cur_min)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        (is_bst, _, _) = self.valid(root)
        return is_bst
