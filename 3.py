class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = {}
        count = 0
        maxCount = 0

        for i in range(len(s)):
            print("i: ", i)
            if s[i] in string and count <= string[s[i]]:
                count = string[s[i]] + 1
                print("count: ", count)
            else:
                maxCount = max(maxCount, i - count + 1)
                print("max: ", maxCount)
            string[s[i]] = i
            print(string)
        
        return maxCount