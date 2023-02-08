from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # return nums == sorted(nums) or nums == sorted(nums, reverse=True)

        if nums[-1] < nums[0]:
            nums = nums[::-1]

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False

        return True
