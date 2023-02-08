import collections
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters = collections.Counter()
        result = []

        for i in licensePlate:
            if i.isalpha():
                letters.update(i.lower())

        for i in words:
            if letters & collections.Counter(i) == letters:
                result.append((len(i), i))

        result.sort(key=lambda x: x[0])

        return result[0][1]
