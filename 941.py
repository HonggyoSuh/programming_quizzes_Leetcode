from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        start, end, length = 0, len(arr) - 1, len(arr)

        while start < length - 1 and arr[start] < arr[start + 1]:
            start += 1
        while end > 0 and arr[end] < arr[end - 1]:
            end -= 1

        return start == end and 0 < start and end < length - 1
