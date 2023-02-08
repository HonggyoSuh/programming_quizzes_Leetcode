from itertools import zip_longest


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # s = s.split()
        # hashmap = {}

        # if len(pattern) != len(s):
        #     return False

        # for index, i in enumerate(pattern):
        #     element = s[index]

        #     if i in hashmap:
        #         if hashmap[i] != element:
        #             return False
        #     elif element in hashmap.values():
        #         return False
        #     else:
        #         hashmap[i] = element

        # return True

        s = s.split()
        return len(set(pattern)) == len(set(s)) == len(set(zip_longest(pattern, s)))
