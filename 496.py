from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = list()

        for i in nums1:
            greater = list(filter(lambda x: x > i, nums2[nums2.index(i):]))
            if (len(greater) == 0): 
                result.append(-1)
            else:
                result.append(greater[0])

        return result
