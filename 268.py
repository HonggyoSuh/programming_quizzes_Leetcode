from functools import reduce
import operator
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()

        # for i in range(0, nums[-1] + 1):
        #     if i not in nums:
        #         return i

        # return nums[-1] + 1

        n = len(nums)
        return int(n * (n + 1) / 2 - sum(nums))

        # return reduce(operator.xor, nums + list(range(len(nums) + 1)))

        # return (set(range(len(nums) + 1)) - set(nums)).pop()
