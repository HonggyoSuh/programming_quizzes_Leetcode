from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]
