#Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. 
#If it is impossible for b to be a substring of a after repeating it, return -1.

#Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".




class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        def lps(string):
            n = len(string)
            lpsarr = [0]*n
            i = 1
            length = 0
            while i < n:
                if string[i] == string[length]:
                    length += 1
                    lpsarr[i] = length
                    i += 1
                else:
                    if length == 0:
                        lpsarr[i] = 0
                        i += 1
                    else:
                        length = lpsarr[length-1]
            return lpsarr
        def kmp(s2,s1):
            lpsarr = lps(s1)
            i = j = 0
            while i < len(s2):
                if s1[j] == s2[i]:
                    i+=1
                    j+=1
                if j == len(s1):
                    return True
                elif i < len(s2) and s1[j] != s2[i]:
                    if j == 0:
                        i += 1
                    else:
                        j = lpsarr[j-1]
        
        k = 0
        m = len(a)
        n = len(b)
        if n > m:
            if n % m == 0:
                k = n//m
            else:
                k = (n//m) + 1
        else:
            k = 0
        count = 1
        store = str(a)
        for i in range(k-1):
            a += str(store)
            count += 1
        for i in range(2): #Very important step, we are only checking two possibilities, one being the lower bound and other lower bound + 1
            if kmp(a,b) == True:
                return count
            else:
                a += str(store)
                count += 1
        return -1
