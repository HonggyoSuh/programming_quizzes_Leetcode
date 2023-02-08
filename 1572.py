from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        length = len(mat)

        for i in range(length):
            total += mat[i][i]
            if not (i == length - i - 1):
                total += mat[i][length - i - 1]
        
        return total