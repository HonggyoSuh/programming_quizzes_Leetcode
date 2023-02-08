from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = set(nums1).union(set(nums2))
        nums3 = list(nums3)
        l = len(nums3)

        if l % 2 == 0:
            return (nums3[l] + nums3[l - 1]) / 2
        else:
            return nums3[l // 2]