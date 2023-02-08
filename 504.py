class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return "0"

        flag = False
        if num < 0:
            flag = True
            num *= -1

        result = []

        while num:
            result.append(str(num % 7))
            num //= 7

        return "-" + "".join(result[::-1]) if flag else "".join(result[::-1])
