import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # for index, i in enumerate(s):
        #     if s.count(i) == 1:
        #         return index

        # return -1

        # hashmap = {}

        # for index, i in enumerate(s):
        #     if i in hashmap:
        #         hashmap[i] += 1
        #     else:
        #         hashmap[i] = 1

        # for i in hashmap:
        #     if hashmap.get(i) == 1:
        #         return s.index(i)

        # return -1

        # counter = collections.Counter(s)

        # for i in counter:
        #     if counter.get(i) == 1:
        #         return s.index(i)

        # return -1

        for i, j in collections.Counter(s).items():
            if j == 1:
                return s.index(i)

        return -1
