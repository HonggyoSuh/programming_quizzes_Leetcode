class Solution:
    def romanToInt(s: str) -> int:
        roman = ["I", "V", "X", "L", "C", "D", "M"]
        integer = [1, 5, 10, 50, 100, 500, 1000]
        prev = ""
        sum = 0

        for i in list(s):
            sum += integer[roman.index(i)]
            # print("sum: ", sum)

            if (prev == "I" and i == "V") or (prev == "I" and i == "X"):
                sum -= 2
                # print("sum - 2")
                
            if (prev == "X" and i == "L") or (prev == "X" and i == "C"):
                sum -= 20
                # print("sum - 20")

            if (prev == "C" and i == "D") or (prev == "C" and i == "M"):
                sum -= 200
                # print("sum - 200")

            prev = i
            
        print(sum)

    if __name__ == "__main__":
        romanToInt(input())