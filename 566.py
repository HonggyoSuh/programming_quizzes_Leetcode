from typing import List
import numpy

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])

        if (row * col != r * c):
            return mat
        
        return numpy.array(mat).reshape(r,c)