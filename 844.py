class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        list_s, list_t = [], []

        for i in s:
            list_s = list_s + [i] if i != "#" else list_s[:-1]

        for i in t:
            list_t = list_t + [i] if i != "#" else list_t[:-1]

        return list_s == list_t
