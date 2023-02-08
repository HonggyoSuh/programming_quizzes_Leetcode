# import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # counter = collections.Counter(nums)
        # max_value = 0
        # max_element = 0

        # for i in counter:
        #     curr_value = counter.get(i)

        #     if curr_value > max_value:
        #         max_value = curr_value
        #         max_element = i

        # return max_element

        # return collections.Counter(nums).most_common()[0][0]

        # return sorted(nums)[len(nums) // 2]

        nums.sort()
        return nums[len(nums) // 2]
