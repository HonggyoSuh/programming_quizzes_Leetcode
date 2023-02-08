from collections import Counter

# from itertools import permutations


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if set.intersection(set(s1), set(s2)) != set(s1) : return False
        # if sorted(list(s1)) == sorted(list(s2)): return True

        # for i in iter(map("".join, permutations(s1, len(s1)))):
        #     if s2.count(i):
        #         return True
        # else:
        #     return False
        # too slow

        if len(s2) < len(s1):
            return False

        s1_counter = Counter(s1)
        s2_sub_counter = Counter(s2[: len(s1)])
        s1_len, s2_len = len(s1), len(s2)

        if s1_counter == s2_sub_counter:
            return True
        for i in range(1, s2_len - s1_len + 1):
            s2_sub_counter[s2[i - 1]] -= 1
            if s2_sub_counter[s2[i - 1]] == 0:
                del s2_sub_counter[s2[i - 1]]
            s2_sub_counter[s2[i + s1_len - 1]] += 1
            if s1_counter == s2_sub_counter:
                return True

        return False
