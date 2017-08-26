# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [('#', -1), (root, 0)]
        left = None
        right = None
        ret = 0
        while len(queue) != 0:
            (node, i) = queue.pop()
            if node == '#':
                if len(queue) == 0:
                    break
                queue.insert(0, ('#', -1))
                left = None
                right = None
            else:
                if left is None:
                    left = i
                if right is None or i > right:
                    right = i
                if node.left is not None:
                    queue.insert(0, (node.left, 2 * i + 1))
                if node.right is not None:
                    queue.insert(0, (node.right, 2 * i + 2))
                if right - left + 1 > ret:
                    ret = right - left + 1
        return ret
