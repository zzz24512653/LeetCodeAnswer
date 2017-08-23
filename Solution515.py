# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        ret = []
        level_max = root.val
        queue = ['#', root]  # 注意顺序!

        while len(queue) != 0:
            node = queue.pop()
            if node == '#':
                ret.append(level_max)
                level_max = float('-inf')
                if len(queue) == 0:
                    break
                else:
                    queue.insert(0, '#')
                    continue
            if node.val > level_max:
                level_max = node.val
            if node.left is not None:
                queue.insert(0, node.left)
            if node.right is not None:
                queue.insert(0, node.right)

        return ret
