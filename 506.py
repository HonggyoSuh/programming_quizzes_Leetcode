from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        hashmap = {i: index for index, i in enumerate(sorted(score, reverse=True))}
        result = []

        for i in score:
            value = hashmap[i]

            if value == 0:
                result.append("Gold Medal")
            elif value == 1:
                result.append("Silver Medal")
            elif value == 2:
                result.append("Bronze Medal")
            else:
                result.append(f"{value + 1}")

        return result
