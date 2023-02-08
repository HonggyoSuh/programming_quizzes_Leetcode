class Solution:
    def findComplement(self, num: int) -> int:
        num = format(num, "b")
        string = ""

        for i in num:
            if int(i):
                string += "0"
            else:
                string += "1"

        return int(string, 2)

        # n = 1

        # while n <= num:
        #     n <<= 1
        # return (n - 1) ^ num
