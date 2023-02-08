from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max(curr_sum, 0) + num
            max_sum = max(max_sum, curr_sum)

        return max_sum
