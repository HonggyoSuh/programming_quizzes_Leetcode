from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for i in range(1, n + 1):
            string = str(i)
            checker1 = sum(map(int, list(string))) % 3 == 0
            checker2 = string[-1] in ["0", "5"]

            if checker1 and checker2:
                result.append("FizzBuzz")
            elif checker1:
                result.append("Fizz")
            elif checker2:
                result.append("Buzz")
            else:
                result.append(str(i))

        return result

        # result = []

        # for i in range(1, n + 1):
        #     if i % 3 == 0 and i % 5 == 0:
        #         result.append("FizzBuzz")
        #     elif i % 3 == 0:
        #         result.append("Fizz")
        #     elif i % 5 == 0:
        #         result.append("Buzz")
        #     else:
        #         result.append(str(i))

        # return result
