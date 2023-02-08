import itertools


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        zipper = itertools.zip_longest(num1[::-1], num2[::-1], fillvalue="0")
        result = 0

        for index, i in enumerate(zipper):
            result += ((ord(i[0]) - 48) * 10**index) + (
                (ord(i[1]) - 48) * 10**index
            )

        return str(result)
