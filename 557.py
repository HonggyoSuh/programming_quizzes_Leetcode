class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        result = ""

        for index, i in enumerate(s):
            result += i[::-1]
            result += " " if index < len(s) - 1 else ""

        return result

        # return " ".join(i[::-1] for i in s.split())
