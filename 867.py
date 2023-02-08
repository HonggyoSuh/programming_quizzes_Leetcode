from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result: List[List[int]] = [[0 for i in matrix] for j in matrix[0]]

        for index1, i in enumerate(matrix):
            for index2, j in enumerate(i):
                result[index2][index1] = j

        return result

        # return zip(*matrix)
