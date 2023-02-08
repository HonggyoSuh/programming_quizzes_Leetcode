class Solution:
    def freqAlphabets(self, s: str) -> str:
        # list_s: list[str] = s.split("#")
        # result = ""

        # for index, i in enumerate(list_s):
        #     if index < len(list_s) - 1:
        #         for j in i[:-2]:
        #             result += chr(int(j) + 96)
        #         result += chr(int(i[-2:]) + 96)
        #     else:
        #         for j in i:
        #             result += chr(int(j) + 96)

        # return result

        for i in range(26, 0, -1):
            s = s.replace(str(i) + "#" * (i >= 10), chr(i + 96))
        return s

        # stack, result = list(s), ""

        # while stack:
        #     char = stack.pop()
        #     if char == "#":
        #         result += chr(int((stack.pop() + stack.pop())[::-1]) + 96)
        #     else:
        #         result += chr(int(char) + 96)

        # return result[::-1]

        # return ''.join(chr(int(i[:2]) + 96) for i in re.findall(r'\d\d#|\d', s))
