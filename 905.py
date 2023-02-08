from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [i for i in nums if i % 2 == 0] + [i for i in nums if i % 2 != 0]

        # if len(nums) == 1:
        #     return nums

        # pointer = 0

        # for index, i in enumerate(nums):
        #     if not i % 2:
        #         if index != pointer:
        #             nums[pointer], nums[index] = nums[index], nums[pointer]
        #         pointer += 1

        # return nums
