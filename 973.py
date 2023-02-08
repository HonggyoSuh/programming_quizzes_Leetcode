from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        points.sort(key=lambda x: sqrt((x[0] ** 2) + (x[1] ** 2)))

        for _ in range(k):
            result.append(points.pop(0))

        return result
