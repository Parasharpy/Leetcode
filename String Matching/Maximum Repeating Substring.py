#For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence.
#The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence.
#If word is not a substring of sequence, word's maximum k-repeating value is 0.

#Given strings sequence and word, return the maximum k-repeating value of word in sequence.


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)
        maxi = n//m
        longest = ""
        for i in range(maxi):
            longest += str(word)
        working = longest + "$" + sequence
        def lpsarr(working):
            x = len(working)
            lps = [0]*x
            i = 1
            length = 0
            while i < x:
                if working[i] == working[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length == 0:
                        i += 1
                    else:
                        length = lps[length-1]
            return lps
        lps = lpsarr(working)
        for i in range(len(working)):
            if working[i] == "$":
                index = i
                
        longest_repeat = max(lps[index+1:])
        return longest_repeat//m
