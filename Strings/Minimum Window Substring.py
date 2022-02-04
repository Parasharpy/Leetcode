#Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) 
#is included in the window. If there is no such substring, return the empty string "".

#The testcases will be generated such that the answer is unique. A substring is a contiguous sequence of characters within the string.


#Input: s = "ADOBECODEBANC", t = "ABC"
#Output: "BANC"
#Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(dictt,mapp):
            if len(dictt) != len(mapp):
                return False
            for x in dictt:
                if dictt[x] != mapp[x]:
                    if dictt[x] > mapp[x]:
                        return False
            return True
        
        m = len(t)
        n = len(s)
        if m > n:
            return ""
        dictt = {}
        mapp = {}
        for i in t:
            if i not in dictt:
                dictt[i] = 1
            else:
                dictt[i] += 1
        for x in range(0,m):
            if s[x] not in mapp and s[x] in dictt:
                mapp[s[x]] = 1
            elif s[x] in dictt and s[x] in mapp:
                mapp[s[x]] += 1
        if dictt == mapp:
            return s[0:m]
        j = 0
        strs = ""
        for i in range(m,n):
            if s[i] in dictt:
                if s[i] in mapp:
                    mapp[s[i]] += 1
                else:
                    mapp[s[i]] = 1
            while check(dictt,mapp) == True:
                if len(strs) < (i-j+1) and len(strs) != 0:
                    strs = strs
                else:
                    strs = str(s[j:i+1])
                if s[j] in mapp and mapp[s[j]] == 1:
                    del mapp[s[j]]
                if s[j] in mapp and mapp[s[j]] > 1:
                    mapp[s[j]] -= 1
                j += 1
        return strs
