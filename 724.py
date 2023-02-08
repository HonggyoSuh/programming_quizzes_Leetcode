from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = [0 for _ in nums]
        right_sum = [0 for _ in nums]
        reverse_nums = nums[::-1]

        for index, (i, j) in enumerate(zip(nums, reverse_nums)):
            if not index:
                continue

            left_sum[index] = left_sum[index - 1] + nums[index - 1]
            right_sum[index] = right_sum[index - 1] + reverse_nums[index - 1]

        for index, i in enumerate(left_sum):
            if i == right_sum[len(right_sum) - index - 1]:
                return index

        return -1

        # left_sum, right_sum = 0, sum(nums)

        # for index, i in enumerate(nums):
        #     right_sum -= i
        #     if left_sum == right_sum:
        #         return index
        #     left_sum += i

        # return -1
