class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        visited = [[False] * n for _ in range(n)]
        ret = 0
        stack = []
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and M[i][j] == 1:
                    ret += 1
                    stack.append((i, j))
                    visited[i][j] = True
                    while len(stack) != 0:
                        (t_i, t_j) = stack.pop()
                        for k in range(n):
                            if not visited[k][t_j] and M[k][t_j] == 1:
                                stack.append((k, t_j))
                                visited[k][t_j] = True
                            if not visited[t_i][k] and M[t_i][k] == 1:
                                stack.append((t_i, k))
                                visited[t_i][k] = True
                visited[i][j] = True
        return ret
