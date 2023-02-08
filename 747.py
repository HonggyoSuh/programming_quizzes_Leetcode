from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums_list = []

        for index, i in enumerate(nums):
            nums_list.append((i, index))

        nums_list.sort(key=lambda x: x[0])

        return nums_list[-1][1] if nums_list[-1][0] >= nums_list[-2][0] * 2 else -1
