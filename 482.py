class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = "".join(s.split("-"))
        left = right = 0
        result = []
        length = len(s)
        leftover = length % k

        if not leftover:
            right = k
        else:
            result.append(s[left:leftover])
            left = leftover
            right = left + k

        while right <= length:
            result.append(s[left:right])
            left += k
            right += k

        return "-".join(result).upper()
