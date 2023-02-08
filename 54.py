import copy
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        copied = copy.deepcopy(matrix)

        while copied:
            temp = copied.pop(0)
            result += temp
            copied = list(zip(*copied))[::-1]
        return result
