class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        split = sentence.split()

        for index, i in enumerate(split):
            if i[0].lower() in "aeiou":
                split[index] = i + "ma" + "a" * (index + 1)
            else:
                split[index] = i[1:] + i[:1] + "ma" + "a" * (index + 1)

        return " ".join(split)
