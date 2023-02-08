class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""

        for i in s:
            n = ord(i)
            result += chr(n + 32) if n >= 65 and n <= 90 else i

        return result
