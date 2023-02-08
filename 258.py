class Solution:
    def addDigits(self, num: int) -> int:
        # if num < 10:
        #     return num
        # string = str(num)
        # result = sum(map(int, list(string)))

        # return self.addDigits(result)

        if not num:
            return num
        elif not num % 9:
            return 9
        else:
            return num % 9
