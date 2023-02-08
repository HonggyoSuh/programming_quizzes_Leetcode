from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = int((sum(aliceSizes) - sum(bobSizes)) / 2)
        aliceSizes, bobSizes = set(aliceSizes), set(bobSizes)

        for i in aliceSizes:
            if i - diff in bobSizes:
                return [i, i - diff]
