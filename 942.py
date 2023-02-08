import collections
from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        left, right = 0, len(s)
        perm = collections.deque()

        for i in s:
            if i == "I":
                perm.append(left)
                left += 1
            else:
                perm.append(right)
                right -= 1
        perm.append(left)

        return perm
