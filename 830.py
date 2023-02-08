from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        current = ""
        count = start = 0
        result = []

        for index, i in enumerate(s):
            if count >= 2:
                if count > 2:
                    result.pop()
                result.append([start, index - 1])
            if i != current:
                current = i
                count = 0
                start = index
            else:
                count += 1

        if count >= 2:
            if count > 2:
                result.pop()
            result.append([start, index])
        return result
