from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [list(map(lambda x: 0 if x else 1, i[::-1])) for i in image]

        # return [reversed(list(map(int, map(operator.not_, row)))) for row in image]
