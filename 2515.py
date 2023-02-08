import sys
from typing import List


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        target_hash = hash(target)
        result = sys.maxsize

        for index, i in enumerate(words):
            if hash(i) == target_hash:
                result = min(
                    result,
                    abs(startIndex - index),
                    len(words) - startIndex + index,
                    len(words) - index + startIndex,
                )

        if result != sys.maxsize:
            return result

        return -1
