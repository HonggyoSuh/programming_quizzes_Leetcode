from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(area**0.5), 0, -1):
            if not area % i:
                return [area // i, i]
