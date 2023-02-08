import collections
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        keys = counter.keys()
        result = 0

        for key in keys:
            if key - 1 in keys:
                value = counter[key - 1] + counter[key]
                if value > result:
                    result = value

        return result
