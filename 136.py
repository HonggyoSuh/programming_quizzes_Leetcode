import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        for i in counter:
            val = counter.get(i)
            if val == 1:
                return i

        return 0

        # set_nums = set()

        # for i in nums:
        #     if i not in set_nums:
        #         set_nums.add(i)
        #     else:
        #         set_nums.remove(i)

        # return set_nums.pop()

        # res = 0

        # for num in nums:
        #     res ^= num

        # return res

        # return 2 * sum(set(nums)) - sum(nums)

        # return reduce(lambda x, y: x ^ y, nums)

        # return reduce(operator.xor, nums)
