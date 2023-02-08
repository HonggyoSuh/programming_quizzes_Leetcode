from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        string = s1.split() + s2.split()

        return [i for i in string if string.count(i) == 1]
