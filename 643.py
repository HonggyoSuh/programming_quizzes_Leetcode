from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = result = sum(nums[:k])

        for i in range(len(nums) - k):
            curr += -nums[i] + nums[i + k]
            if curr > result:
                result = curr

        return result / k
