#Given a string s, find the length of the longest substring without repeating characters.
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictt = {}
        j = 0
        length = 0
        for i in range(len(s)):
            if s[i] not in dictt:
                dictt[s[i]] = 1
            else:
                while s[i] in dictt:
                    if dictt[s[j]] == 1:
                        del dictt[s[j]]
                    else:
                        dictt[s[j]] -= 1
                    j += 1
                dictt[s[i]] = 1
            length = max(length, (i - j + 1))
        return length
