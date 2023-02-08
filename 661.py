from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row, col = len(img), len(img[0])
        result = [[0 for i in img[0]] for j in img]
        direction = [
            [0, 0],
            [0, 1],
            [0, -1],
            [1, 0],
            [1, 1],
            [1, -1],
            [-1, 0],
            [-1, 1],
            [-1, -1],
        ]

        for index1, i in enumerate(img):
            for index2, j in enumerate(i):
                temp = [
                    img[index1 + m][index2 + n]
                    for m, n in direction
                    if 0 <= index1 + m < row and 0 <= index2 + n < col
                ]
                result[index1][index2] = sum(temp) // len(temp)

        return result
