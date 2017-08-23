"""
思路一开始基本上是对的,但是搜索方法不好,导致多次超时。
开始时是从每个0开始更新它能影响到的点,但是最优的策略是先修改距离为1的再修改距离为2的依次前进。
"""


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(matrix)
        m = len(matrix[0])
        ret = [[None] * m for _ in range(n)]

        queue = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    ret[i][j] = 0
                    queue.insert(0, (i, j))

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while len(queue) != 0:
            (i, j) = queue.pop()
            for offset1, offset2 in directions:
                cur_i = i + offset1
                cur_j = j + offset2
                if cur_i < 0 or cur_i >= n or cur_j < 0 or cur_j >= m:
                    continue
                if ret[cur_i][cur_j] is not None and ret[cur_i][cur_j] <= ret[i][j]+1:
                    continue
                ret[cur_i][cur_j] = ret[i][j] + 1
                queue.insert(0, (cur_i, cur_j))

        return ret
