class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(" ")
        l = len(s)
        num = []
        result = []
        string = ""
        for i in range(10):
            num.append(str(i))
        flag = False
        flag2 = False
        count = 0

        for i in range(l):
            if s[i] == "-":
                if flag2:
                    break

                flag = True
                count += 1

                if count >= 2:
                    break
            elif s[i] == "+":
                count += 1

                if count >= 2 or flag2:
                    break
            elif s[i] in num:
                result.append(s[i])
                flag2 = True
            else:
                break

        for i in range(len(result)):
            string += result[i]

        if len(string) != 0:
            string = int(string)
        else:
            return 0

        # if flag:
        # string -= string

        # if string > 2**31 - 1:
        #     return 2**31 - 1
        # elif string < -(2**31):
        #     return -(2**31)
        # else:
        #     return string
