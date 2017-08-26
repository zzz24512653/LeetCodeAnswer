class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(M)
        m = len(M[0])
        ret = []
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0),(1,1)]
        for i in range(n):
            line = []
            for j in range(m):
                cur_sum = 0
                cur_cnt = 0
                for (move_i, move_j) in directions:
                    cur_i = i + move_i
                    cur_j = j + move_j
                    if cur_i >= n or cur_i < 0 or cur_j >= m or cur_j < 0:
                        continue
                    cur_sum += M[cur_i][cur_j]
                    cur_cnt += 1
                line.append(int(cur_sum/cur_cnt))
            ret.append(line)
        return ret
