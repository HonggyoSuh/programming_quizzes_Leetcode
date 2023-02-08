class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if len(needle) > len(haystack):
        #     return -1

        # for i in range(len(haystack) - len(needle) + 1):
        #     if needle == haystack[i : len(needle) + i]:
        #         return i

        # return -1

        # return haystack.find(needle)

        # if len(needle) > len(haystack):
        #     return -1

        # needle_hash = hash(needle)
        # for i in range(len(haystack) - len(needle) + 1):
        #     substring = haystack[i : len(needle) + i]
        #     if needle_hash == hash(substring) and needle == substring:
        #         return i

        # return -1

        table = [0 for _ in range(len(needle))]
        i = 0

        for j in range(1, len(needle)):
            while i > 0 and needle[i] != needle[j]:
                i = table[i - 1]

            if needle[i] == needle[j]:
                i += 1
                table[j] = i

        i = 0
        for j in range(len(haystack)):
            while i > 0 and needle[i] != haystack[j]:
                i = table[i - 1]

            if needle[i] == haystack[j]:
                i += 1
                if i == len(needle):
                    return j - i + 1

        return -1
