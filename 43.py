class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int_num1 = 0
        int_num2 = 0

        for index, i in enumerate(num1):
            int_num1 += (ord(i) - 48) * (10 ** (len(num1) - index - 1))

        for index, i in enumerate(num2):
            int_num2 += (ord(i) - 48) * (10 ** (len(num2) - index - 1))

        return str(int_num1 * int_num2)
