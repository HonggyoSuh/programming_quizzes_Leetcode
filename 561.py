from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # nums.sort()
        # result = 0

        # for index, i in enumerate(nums):
        #     if index == 0 or index % 2 == 0:
        #         result += i

        # return result

        return sum(sorted(nums)[::2])
