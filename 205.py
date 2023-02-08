class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # hashmap = {}

        # for (i, j) in zip(s, t):
        #     if i in hashmap.keys() and hashmap[i] != j:
        #         return False
        #     elif j in hashmap.values() and i not in (
        #         k for k, v in hashmap.items() if v == j
        #     ):
        #         return False

        #     hashmap[i] = j

        # return True

        # return list(map(s.find, s)) == list(map(t.find, t))

        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

        # return [s.find(i) for i in s] == [t.find(j) for j in t]
