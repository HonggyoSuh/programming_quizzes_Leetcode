from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])


# import numpy

# class Solution:
#     def maximumProduct(self, nums: List[int]) -> int:
#         large_queue = heapq.nlargest(3, nums)
#         small_queue = heapq.nsmallest(2, nums)

#         return max(numpy.prod(large_queue), numpy.prod(small_queue) * large_queue[0])
