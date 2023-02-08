from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        last = 0

        for i in flowerbed:
            if i == 1:
                if last == 1:
                    n += 1
                last = 1
            else:
                if last == 1:
                    last = 0
                else:
                    n -= 1
                    last = 1

        return n <= 0
