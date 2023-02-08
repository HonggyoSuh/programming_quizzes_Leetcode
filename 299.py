import collections
import operator


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = cow = 0
        counter1 = collections.Counter(secret)
        counter2 = collections.Counter(guess)

        bull = sum(map(operator.eq, secret, guess))

        for i in set(secret):
            if counter1.get(i) and counter2.get(i):
                cow += min(counter1.get(i), counter2.get(i))

        return f"{bull}A{cow - bull}B"
