from collections import Counter
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # words = {}
        # paragraph = paragraph.replace(",", " ")

        # for i in paragraph.split():
        #     temp = i.lower()
        #     temp = temp.strip(" !?',;.")

        #     if temp not in banned:
        #         if temp not in words:
        #             words[temp] = 0
        #         words[temp] += 1

        # return max(words, key=words.get)

        return Counter(
            [
                word.lower()
                for word in re.compile("\w+").findall(paragraph)
                if word.lower() not in banned
            ]
        ).most_common()[0][0]
