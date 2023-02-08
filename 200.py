from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        max_row, max_col = len(grid), len(grid[0])
        result = 0

        for index1, i in enumerate(grid):
            for index2, j in enumerate(i):
                if j == "1":
                    self.find_island(index1, index2, max_row, max_col, grid)
                    result += 1

        return result

    def find_island(
        self,
        index1: int,
        index2: int,
        max_row: int,
        max_col: int,
        grid: List[List[str]],
    ) -> int:
        if index1 >= max_row or index1 < 0 or index2 >= max_col or index2 < 0:
            return

        if grid[index1][index2] == "1":
            grid[index1][index2] = "2"
            self.find_island(index1 - 1, index2, max_row, max_col, grid)
            self.find_island(index1, index2 - 1, max_row, max_col, grid)
            self.find_island(index1 + 1, index2, max_row, max_col, grid)
            self.find_island(index1, index2 + 1, max_row, max_col, grid)
