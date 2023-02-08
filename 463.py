from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0

        for row, i in enumerate(grid):
            for col, i in enumerate(i):
                if grid[row][col]:
                    result += 4
                    if row and grid[row - 1][col]:
                        result -= 2
                    if col and grid[row][col - 1]:
                        result -= 2
        return result
