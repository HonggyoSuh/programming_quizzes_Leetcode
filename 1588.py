import collections
import itertools
from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0

        for i in range(1, len(arr) + 1):
            if i % 2 != 0:
                for j in Solution().sliding_window(arr, i):
                    res += sum(j)

        return res

    def sliding_window(self, iterable, n):
        it = iter(iterable)
        window = collections.deque(itertools.islice(it, n), maxlen = n)
        if len(window) == n:
            yield tuple(window)
        for x in it:
            window.append(x)
            yield tuple(window)