import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return itertools.combinations(range(1, n + 1), k)

        # combs = [[]]
        # for _ in range(k):
        #     combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
        # return combs

        # return reduce(lambda C, _: [[i]+c for c in C for i in range(1, c[0] if c else n+1)],
        #           range(k), [[]])
