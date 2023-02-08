import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return (collections.Counter(nums1) & collections.Counter(nums2)).elements()

        # nums1.sort()
        # nums2.sort()
        # result = []
        # p1 = p2 = 0

        # while p1 < len(nums1) and p2 < len(nums2):
        #     if nums1[p1] < nums2[p2]:
        #         p1 += 1
        #     elif nums2[p2] < nums1[p1]:
        #         p2 += 1
        #     else:
        #         result.append(nums1[p1])
        #         p1 += 1
        #         p2 += 1

        # return result
