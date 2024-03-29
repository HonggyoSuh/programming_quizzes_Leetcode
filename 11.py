from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, width, result = 0, len(height) - 1, len(height) - 1, 0

        for w in range(width, 0, -1):
            if height[left] < height[right]:
                result = max(result, height[left] * w)
                left += 1
            else:
                result = max(result, height[right] * w)
                right -= 1
        
        return result