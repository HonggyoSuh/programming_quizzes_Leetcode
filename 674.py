from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        result, curr, prev = 1, 1, nums[0]

        for i in nums[1:]:
            if i > prev:
                curr += 1
                if curr > result:
                    result = curr
                prev = i
            else:
                prev = i
                curr = 1

        return result
