from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ii, i = 0, 1
        while ii < len(nums) and i < len(nums):
            if not nums[ii] & 1:
                ii += 2
            elif nums[i] & 1:
                i += 2
            else:
                nums[ii], nums[i] = nums[i], nums[ii]
                ii += 2
                i += 2
        return nums
