from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0] for _ in nums]

        for index, i in enumerate(nums):
            if not index:
                continue

            result[index] = i + result[index - 1]

        return result
