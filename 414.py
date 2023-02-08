from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # nums.sort(reverse=True)
        # maximum = nums[0]

        # if len(set(nums)) < 3:
        #     return maximum

        # count = 0
        # for i in nums[1:]:
        #     if count == 2:
        #         break
        #     if maximum != i:
        #         maximum = i
        #         count += 1

        # return maximum

        nums = sorted(set(nums), reverse=True)

        if len(nums) >= 3:
            return nums[2]
        else:
            return nums[0]
