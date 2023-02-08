from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return set(nums1).intersection(set(nums2))

        # result = []
        # nums1.sort()
        # nums2.sort()
        # i = j = 0

        # while i < len(nums1) and j < len(nums2):
        #     first, second = nums1[i], nums2[j]

        #     if first > second:
        #         j += 1
        #     elif first < second:
        #         i += 1
        #     else:
        #         if first not in result:
        #             result.append(first)
        #         i += 1
        #         j += 1

        # return result

        s = set()
        ans = []
        for num in nums1:
            s.add(num)
        for num in nums2:
            if num in s:
                ans.append(num)
                s.remove(num)
        return ans
