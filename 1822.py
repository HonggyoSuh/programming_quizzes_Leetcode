from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
    #     nums = list(1 if i > 0 else 0 if i == 0 else -1 for i in nums)
    #     return Solution().signFunc(numpy.prod(nums))

    # def signFunc(self, x: int) -> int:
    #     return 1 if x > 0 else 0 if x == 0 else -1
        return 0 if 0 in nums else -1 if sum(x < 0 for x in nums) % 2 else 1