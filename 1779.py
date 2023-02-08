from typing import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        minValue = 0
        minIndex = 0
        flag = False

        for index, i in enumerate(points):
            if x == i[0] or y == i[1]:
                temp = abs(x - i[0]) + abs(y - i[1])

                if minValue > temp:
                    minValue = temp
                    minIndex = index
                    flag = True
            
        if flag:
            return minIndex
        else:
            return -1
            

