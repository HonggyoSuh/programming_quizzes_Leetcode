from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit, curr, result = deque(), deque(), 0

        for index1, i in enumerate(grid):
            for index2, j in enumerate(i):
                if j == 1:
                    visit.append((index1, index2))
                elif j == 2:
                    curr.append((index1, index2))

        while visit and curr:
            for _ in range(len(curr)):
                i, j = curr.popleft()

                for coordinate in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if coordinate in visit:
                        visit.remove(coordinate)
                        curr.append(coordinate)
            result += 1

        return -1 if visit else result
