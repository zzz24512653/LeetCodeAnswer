# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left_most = root.val
        new_line = False
        queue = ['#', root]
        while len(queue) != 0:
            node = queue.pop()
            if node == '#':
                if len(queue) == 0:
                    break
                else:
                    new_line = True
                    queue.insert(0, '#')
                    continue
            if new_line:
                left_most = node.val
                new_line = False
            if node.left is not None:
                queue.insert(0, node.left)
            if node.right is not None:
                queue.insert(0, node.right)
        return left_most
