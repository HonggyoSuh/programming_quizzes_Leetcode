# import itertools
from typing import List

class Solution:
    # def largestPerimeter(self, nums: List[int]) -> int:
    #     return max(Solution().perimeter(list(i)) for i in itertools.combinations(nums, 3))
    
    # def perimeter(self, comb: List[int]) -> int:
    #     side = max(comb)
    #     comb.remove(side)
        
    #     return sum(comb) + side if sum(comb) > side else 0
        
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        l = len(nums)
        
        for i in range(l - 3):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return sum(nums[i : i + 3])