import collections
from functools import reduce
import math
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return reduce(math.gcd, collections.Counter(deck).values()) != 1

        # return math.gcd(*collections.Counter(deck).values()) != 1
