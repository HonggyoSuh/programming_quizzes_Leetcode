import collections
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        counter.most_common()

        return sorted([i for i in counter], key=lambda x: (-counter.get(x), x.lower()))[
            :k
        ]
