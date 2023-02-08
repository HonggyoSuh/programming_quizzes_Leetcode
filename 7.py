class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -x
            x = str(x)
            x = x[::-1]
            x.lstrip("0")
            x = int(x)

            if x < -2 ** 31 or x > 2 ** 31 - 1:
                return 0
            else: 
                return -x
        else:
            x = str(x)
            x = x[::-1]
            x.lstrip("0")
            x = int(x)

            if x < -2 ** 31 or x > 2 ** 31 - 1:
                return 0
            else: 
                return x