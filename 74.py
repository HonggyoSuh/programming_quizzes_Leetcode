from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # return any(target in row for row in matrix)

        return any(target in row for row in matrix if row[-1] >= target)

        # r = bisect_left(
        #     matrix, target, key=lambda row: row[-1]
        # )  # or key=itemgetter(-1)
        # return r < len(matrix) and matrix[r][bisect_left(matrix[r], target)] == target

        # n = len(matrix[0])

        # def get(idx: int) -> int:
        #     r, c = divmod(idx, n)
        #     return matrix[r][c]

        # return get(bisect_left(range(len(matrix) * n - 1), target, key=get)) == target
