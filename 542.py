from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        m = len(mat)
        n = len(mat[0])

        for index1, i in enumerate(mat):
            for index2, j in enumerate(i):
                if not mat[index1][index2]:
                    queue.append((index1, index2))
                else:
                    mat[index1][index2] = -1

        while queue:
            x, y = queue.popleft()

            for row, col in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + row, y + col

                if 0 <= new_x < m and 0 <= new_y < n and mat[new_x][new_y] == -1:
                    mat[new_x][new_y] = mat[x][y] + 1
                    queue.append((new_x, new_y))

        return mat
