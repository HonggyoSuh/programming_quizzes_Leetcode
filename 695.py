from typing import List


class Solution:
    def calc_area(
        self, copy: List[List[int]], i: int, j: int, row_max: int, col_max: int
    ) -> int:
        if i < 0 or i >= row_max or j < 0 or j >= col_max:
            return 0
        if copy[i][j] != 1:
            return 0
        copy[i][j] = 2

        return (
            1
            + self.calc_area(copy, i - 1, j, row_max, col_max)
            + self.calc_area(copy, i + 1, j, row_max, col_max)
            + self.calc_area(copy, i, j - 1, row_max, col_max)
            + self.calc_area(copy, i, j + 1, row_max, col_max)
        )

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        copy = grid
        max_area = 0
        row_max = len(copy)
        col_max = len(copy[0])

        for index1, i in enumerate(grid):
            for index2, j in enumerate(i):
                if copy[index1][index2] == 1:
                    max_area = max(
                        max_area, self.calc_area(copy, index1, index2, row_max, col_max)
                    )

        return max_area
