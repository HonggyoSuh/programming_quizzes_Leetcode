from collections import deque
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        queue = deque(operations)
        result = []

        while queue:
            element = queue.popleft()

            if element == "C":
                result.pop()
            elif element == "D":
                result.append(result[-1] * 2)
            elif element == "+":
                result.append(result[-1] + result[-2])
            else:
                result.append(int(element))

        return sum(result)
