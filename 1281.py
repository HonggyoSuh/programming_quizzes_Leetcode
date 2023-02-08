class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        string = str(n)
        sum = 0
        mul = 1

        for i in range(len(string)):
            sum += int(string[i])
            mul *= int(string[i])

        return mul - sum