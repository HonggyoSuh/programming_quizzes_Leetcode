from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        l = len(coordinates)
        ratio = Solution().calcRatio(coordinates[0], coordinates[1])

        if l == 2: return True

        for i in range(l - 1):
            if Solution().calcRatio(coordinates[i], coordinates[i + 1]) != ratio:
                return False
        
        return True

    def calcRatio(self, x: List[int], y: List[int]) -> float:
        return (y[1] - x[1]) / (y[0] - x[0]) if (y[0] - x[0]) != 0 else -1