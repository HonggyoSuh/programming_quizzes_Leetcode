import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = collections.defaultdict(int)

        for right in range(len(s)):
            count[s[right]] += 1
            elements = right - left + 1

            if elements - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

        return right - left + 1
