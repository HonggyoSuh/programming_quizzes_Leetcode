import collections
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        duplicate = collections.Counter(nums).most_common(1)[0][0]
        nums.remove(duplicate)
        missing = int((n * (n + 1)) / 2 - sum(nums))
        return [duplicate, missing]

        # n, a, b = len(nums), sum(nums), sum(set(nums))
        # s = int(n * (n + 1) / 2)

        # return [a - b, s - b]
