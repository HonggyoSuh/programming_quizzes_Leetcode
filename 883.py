from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        # return (
        #     sum(sum(j != 0 for j in i) for i in grid)
        #     + sum(max(i) for i in zip(*grid))
        #     + sum(max(i) for i in grid)
        # )

        return sum(len(i) - i.count(0) + max(i) for i in grid) + sum(
            max(i) for i in zip(*grid)
        )
