from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # hashmap = {}

        # for index, value in enumerate(nums):
        #     if value in hashmap and index - hashmap[value] <= k:
        #         return True
        #     hashmap[value] = index

        # return False

        num_set = set()

        for index, value in enumerate(nums):
            if value in num_set:
                return True

            num_set.add(value)

            if len(num_set) > k:
                num_set.remove(nums[index - k])

        return False
