from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        for i in range(left, right + 1):
            string = str(i)

            if "0" not in string and all(i % int(j) == 0 for j in string):
                result.append(i)

        return result
