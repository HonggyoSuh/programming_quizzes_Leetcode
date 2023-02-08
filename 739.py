from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result, stack = [0] * len(temperatures), []

        for index, value in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperatures[index]:
                result[stack.pop()] = index - stack[-1]
            stack.append(index)
        return result
